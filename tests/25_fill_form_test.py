from datetime import timedelta, time, datetime, date

import pytest

from gforms import Form
from gforms.elements_base import Grid
from gforms.elements import DateTime, Duration, Date, Time
from gforms.errors import FormNotLoaded, FormNotValidated

from .conftest import FormDumpTest


# NOTE will most probably fail if elements aren't parsed correctly
# Xfail this class if any test_elements() in 10_load_test fails?
class TestFill(FormDumpTest):
    """
    A form with all types of input elements.
    Ones that can be filled by default_callback (choice types) are marked as required.
    Ones that cannot be filled, are not required.
    The elements are split into three pages by type:
    text input elements, choice elements and date/time elements.
    There is also a fourth page containing only a comment element and nn empty fifth page.
    For each text or choice element, "1" is a valid input (or list of "1"'s for a grid)
    """

    form_type = 'fill'

    @staticmethod
    def custom_callback(elem, _, __):
        # return a valid non-empty value for any element
        if isinstance(elem, Date):
            return date(1, 1, 1)
        if isinstance(elem, DateTime):
            return datetime(1, 1, 1, 1, 1)
        if isinstance(elem, Time):
            return time(1, 1)
        if isinstance(elem, Duration):
            return timedelta(hours=1, minutes=1, seconds=1)
        if isinstance(elem, Grid):
            return ['1'] * len(elem.rows)
        return '1'

    def test_fill_default(self, form):
        form.fill()

    def test_fill_with_optional(self, form):
        # Check that the default callback was invoked on at least one optional element
        # Optional elements in this form cannot be filled by the default callback
        with pytest.raises(NotImplementedError):
            form.fill(fill_optional=True)

    def test_fill_callback(self, form):
        form.fill(self.custom_callback)

    def test_callback_missing_return(self, form):
        with pytest.raises(ValueError, match=r'missing.+return statement'):
            form.fill(lambda e, i, j: None)

    def test_to_str_filled(self, form):
        # NOTE These tests only assert that to_str doesn't fail. The return value is not checked
        form.fill(self.custom_callback)
        _ = form.to_str(include_answer=True)


class TestFillNotLoaded:
    def test_fill_not_loaded(self):
        form = Form()
        with pytest.raises(FormNotLoaded):
            form.fill()


class TestSubmitErrors(FormDumpTest):
    form_type = 'fill'

    def test_submit_not_loaded(self):
        form = Form()
        with pytest.raises(FormNotLoaded):
            form.submit()

    def test_submit_not_validated(self, form):
        # may contain loops or contains unvalidated elements
        with pytest.raises(FormNotValidated):
            form.submit()


class Test1PageValidation(FormDumpTest):
    form_type = 'required'

    def test_not_validated(self, form):  # failed in 1.1.2
        # contains unvalidated elements, path/loop check is not required
        with pytest.raises(FormNotValidated):
            form.submit()


class TestInvalidation(FormDumpTest):
    """
    The form has two pages.
    The first page contains a short text input and a radio input
    with options "Loop" (go to page 1) and "Next" (go to next page).
    Both elements are optional.
    The second page contains a radio input (a copy of the first one).
    """

    form_type = 'form_validation'

    def test_element_invalidation(self, form):
        form.validate()  # will pass, since the elements are optional
        assert form.is_validated
        short = form.pages[0].elements[0]
        short.set_value('some_text')
        assert not form.is_validated
        short.validate()
        assert form.is_validated

    def test_path_invalidation(self, form):
        form.validate()
        assert form.is_validated
        radio = form.pages[0].elements[1]
        radio.set_value('Next')
        radio.validate()
        # If an element has actions and they are not ignored,
        # the whole form needs to be validated.
        assert not form.is_validated
        form.validate()
        assert form.is_validated
        # Ignored actions should not invalidate an existing path
        radio2 = form.pages[1].elements[0]
        radio2.set_value('Loop')
        radio2.validate()
        assert form.is_validated


class TestMultipageValidation(FormDumpTest):
    """
    The form has three pages.
    The first page contains a required radio input with options
    "Next" (go to next page) and "Skip" (go page 3).
    The second (skippable) page contains a required radio input.
    The third page is empty.
    """

    form_type = 'multipage_validation'

    def test_skipped_page(self, form):
        radio = form.pages[0].elements[0]
        radio.set_value('Skip')
        radio2 = form.pages[1].elements[0]
        radio2.set_value('Opt1')
        form.validate()
        # Skipped page is not validated, but this should not affect form status
        assert form.is_validated  # failed in 1.1.2
        form.pages[1].validate()
        # Skipped page invalidation should not affect form status
        radio2.set_value('Opt2')
        assert form.is_validated
