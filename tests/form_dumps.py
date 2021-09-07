from .fake_urls import _yt_link, ResponseId


class FDMeta(type):
    def __getattr__(cls, key):
        return getattr(cls._types[key], key)


class FormData(metaclass=FDMeta):
    class _CatMeta(type):
        def __iter__(cls):
            for name in cls.__dict__:
                if not name.startswith('_'):
                    yield name

    class _Category(metaclass=_CatMeta):
        pass

    class Elements(_Category):
        empty = [None, ['Form_description', None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, 'Form_title', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '01_Empty', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        pages = [None, [None, [[1326917918, 'Page02', 'Page02_descr', 8, None, -2], [1315023666, 'Page03', None, 8, None, -1], [1113666652, 'Page04', None, 8, None, 1326917918], [1201871679, 'Page05', None, 8, None, 1113666652], [332799554, 'Page06', None, 8, None, 332799554], [1071355653, 'Page07', None, 8, None, -3]], ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '02_Pages', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '02_Pages', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        elements = [None, [None, [[1443236733, 'Short', 'Short_descr', 0, [[1248303100, None, 0]]], [1507412896, 'Paragraph', 'Paragraph_descr', 1, [[1619539708, None, 0]]], [1049944311, 'Radio', 'Radio_descr', 2, [[332556401, [['Option 1']], 0, None, None, None, None, None, 0]]], [2127891336, 'Checkboxes', 'Checkboxes_descr', 4, [[1438759666, [['Option 1']], 0, None, None, None, None, None, 0]]], [1131290307, 'Dropdown', 'Dropdown_descr', 3, [[2136926694, [['Option 1']], 0, None, None, None, None, None, 0]]], [223940975, 'Scale', 'Scale_descr', 5, [[1371014301, [['1'], ['2'], ['3'], ['4'], ['5']], 0, ['', '']]]], [1656954276, 'RadioGrid', 'RadioGrid_descr', 7, [[1137920119, [['Column 1']], 0, ['Row 1'], None, None, None, None, None, None, None, [0]]]], [1913703271, 'CheckboxGrid', 'CheckboxGrid_descr', 7, [[476435380, [['Column 1']], 0, ['Row 1'], None, None, None, None, None, None, None, [1]]]], [1961232716, 'Date', 'Date_descr', 9, [[1562945923, None, 0, None, None, None, None, [0, 1]]]], [767975817, 'DateTime', 'DateTime_descr', 9, [[1952395559, None, 0, None, None, None, None, [1, 1]]]], [804646304, 'Time', 'Time_descr', 10, [[762776891, None, 0, None, None, None, [0]]]], [1760302336, 'Duration', 'Duration_descr', 10, [[163457168, None, 0, None, None, None, [1]]]], [1299644102, 'Comment', 'Comment_descr', 6], [207969198, 'Image', 'Image_descr', 11, None, None, ['000000000000000000000000000000000000000000000000', 0, [150, 150, 0]]], [1311212999, 'Video', 'Video_descr', 12, None, None, [None, 1, [320, 180, 0], _yt_link]]], None, None, None, [0, 0], None, [1, ''], '02.1_Elements', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '02.1_Elements', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        non_input = [None, [None, [[1417070551, 'Comment', 'Comment_descr', 6], [1142925453, 'Image', 'Image_descr', 11, None, None, ['000000000000000000000000000000000000000000000000', 0, [150, 150, 0]]], [1559999115, 'Video', 'Video_descr', 12, None, None, [None, 1, [320, 180, 0], _yt_link]]], None, None, None, [0, 0], None, None, '03_NonInput', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '03_NonInput', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        text = [None, [None, [[1740905320, 'Short', 'Short_descr', 0, [[466999339, None, 0]]], [963123062, 'Paragraph', 'Paragraph_descr', 1, [[1683892096, None, 0]]]], None, None, None, [0, 0], None, None, '04_Text', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '04_Text', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        required = [None, [None, [[994204884, 'Short_required', None, 0, [[1882437818, None, 1]]], [2093887708, 'Short_optional', None, 0, [[1925578768, None, 0]]]], None, None, None, [0, 0], None, None, '05_Required', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '05_Required', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        radio = [None, [None, [[1300240451, 'Radio', 'Radio_descr', 2, [[746016953, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['Opt3', None, None, None, 0]], 0, None, None, None, None, None, 0]]], [2128921736, 'Radio_other', None, 2, [[1093560649, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['Opt3', None, None, None, 0], ['', None, None, None, 1]], 0, None, None, None, None, None, 0]]], [82100411, 'Radio_actions_other', None, 2, [[662883479, [['Opt1', None, -2, None, 0], ['Opt2', None, -1, None, 0], ['Opt3', None, -2, None, 0], ['', None, -3, None, 1]], 0, None, None, None, None, None, 0]]], [169992643, 'Page2', None, 8, None, -2], [1605896725, 'Radio_actions_other_ignored', None, 2, [[336799860, [['Opt1', None, -2, None, 0], ['Opt2', None, -1, None, 0], ['Opt3', None, -2, None, 0], ['', None, -3, None, 1]], 0, None, None, None, None, None, 0]]]], None, None, None, [0, 0], None, None, '06_Radio', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '06_Radio', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        dropdown = [None, [None, [[1811170342, 'Dropdown', None, 3, [[170607496, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['Opt3', None, None, None, 0], ['Opt4', None, None, None, 0]], 0, None, None, None, None, None, 0]]], [1583172264, 'Dropdown_actions', None, 3, [[1153354260, [['Opt1', None, -2, None, 0], ['Opt2', None, -1, None, 0], ['Opt3', None, 650339404, None, 0], ['Opt4', None, -3, None, 0]], 0, None, None, None, None, None, 0]]], [650339404, 'Untitled Section', None, 8], [2025736661, 'Ignored_actions', None, 3, [[1523567200, [['Opt1', None, -2, None, 0], ['Opt2', None, -1, None, 0], ['Opt3', None, 650339404, None, 0], ['Opt4', None, -3, None, 0]], 0, None, None, None, None, None, 0]]]], None, None, None, [0, 0], None, None, '07_Dropdown', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '07_Dropdown', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        checkboxes = [None, [None, [[676893755, 'Checkboxes', None, 4, [[1678607799, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0]], 0, None, None, None, None, None, 0]]], [2063098907, 'Checkboxes_other', None, 4, [[1813650856, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['', None, None, None, 1]], 0, None, None, None, None, None, 0]]]], None, None, None, [0, 0], None, None, '08_Checkboxes', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '08_Checkboxes', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        scale = [None, [None, [[1366805923, 'Scale_1_5', None, 5, [[408167357, [['1'], ['2'], ['3'], ['4'], ['5']], 0, ['Low', 'High']]]], [753840873, 'Scale_1_10', None, 5, [[896646761, [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10']], 0, ['Low', 'High']]]]], None, None, None, [0, 0], None, None, '09_Scale', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '09_Scale', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        grid = [None, [None, [[955865352, 'RadioGrid', None, 7, [[1502737968, [['C1'], ['C2'], ['C3']], 0, ['R1'], None, None, None, None, None, None, None, [0]], [74462378, [['C1'], ['C2'], ['C3']], 0, ['R2'], None, None, None, None, None, None, None, [0]], [1175051493, [['C1'], ['C2'], ['C3']], 0, ['R3'], None, None, None, None, None, None, None, [0]]]], [224886489, 'CheckboxGrid', None, 7, [[611568981, [['C1'], ['C2'], ['C3']], 0, ['R1'], None, None, None, None, None, None, None, [1]], [261934749, [['C1'], ['C2'], ['C3']], 0, ['R2'], None, None, None, None, None, None, None, [1]], [1002675128, [['C1'], ['C2'], ['C3']], 0, ['R3'], None, None, None, None, None, None, None, [1]]]]], None, None, None, [0, 0], None, None, '10_Grid', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '10_Grid', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        date = [None, [None, [[1903533129, 'YMD', None, 9, [[1237528892, None, 0, None, None, None, None, [0, 1]]]], [1741111285, 'YMDT', None, 9, [[7443757, None, 0, None, None, None, None, [1, 1]]]], [2128840883, 'MD', None, 9, [[1864335203, None, 0, None, None, None, None, [0, 0]]]], [1697995903, 'MDT', None, 9, [[2147130957, None, 0, None, None, None, None, [1, 0]]]]], None, None, None, [0, 0], None, None, '11_Date', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '11_Date', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        time = [None, [None, [[2057065358, 'Time', None, 10, [[524350143, None, 0, None, None, None, [0]]]], [1608541660, 'Duration', None, 10, [[1258054451, None, 0, None, None, None, [1]]]]], None, None, None, [0, 0], None, None, '12_Time', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '12_Time', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]

        text_validation = [None, [None, [[1184612050, 'Custom_error', None, 0, [[63135660, None, 0, None, [[1, 1, ['123'], 'Error_text']]]]], [803234991, 'Number_gt', None, 0, [[198404530, None, 0, None, [[1, 1, ['123']]]]]], [744974129, 'Number_ge', None, 0, [[207152299, None, 0, None, [[1, 2, ['123']]]]]], [1351482554, 'Number_lt', None, 0, [[82872645, None, 0, None, [[1, 3, ['123']]]]]], [318489673, 'Number_le', None, 0, [[792631885, None, 0, None, [[1, 4, ['123']]]]]], [328715370, 'Number_eq', None, 0, [[1405561011, None, 0, None, [[1, 5, ['123']]]]]], [1508928313, 'Number_ne', None, 0, [[1280569314, None, 0, None, [[1, 6, ['123']]]]]], [1876515655, 'Number_range', None, 0, [[1902512540, None, 0, None, [[1, 7, ['123', '456']]]]]], [1346529332, 'Number_nrange', None, 0, [[2144561454, None, 0, None, [[1, 8, ['123', '456']]]]]], [1153262989, 'Number', None, 0, [[1825563315, None, 0, None, [[1, 9]]]]], [226986154, 'Int', None, 0, [[52261562, None, 0, None, [[1, 10]]]]], [1652129975, 'Text_contains', None, 0, [[1942375871, None, 0, None, [[2, 100, ['qwe']]]]]], [883755782, 'Text_ncontains', None, 0, [[1940593378, None, 0, None, [[2, 101, ['qwe']]]]]], [604187219, 'Text_email', None, 0, [[1569187919, None, 0, None, [[2, 102]]]]], [314331766, 'Text_url', None, 0, [[1993959788, None, 0, None, [[2, 103]]]]], [306564057, 'Max_len', None, 0, [[1473696152, None, 0, None, [[6, 202, ['123']]]]]], [1908466015, 'Min_len', None, 0, [[1479951566, None, 0, None, [[6, 203, ['123']]]]]], [87773135, 'Re_search', None, 0, [[1797032676, None, 0, None, [[4, 299, ['qw.rt[a-z]']]]]]], [1549605126, 'Re_nsearch', None, 0, [[1030363843, None, 0, None, [[4, 300, ['qw.rt[a-z]']]]]]], [899038467, 'Re_match', None, 0, [[285042296, None, 0, None, [[4, 301, ['qw.rt[a-z]']]]]]], [2059214362, 'Re_nmatch', None, 0, [[1526467033, None, 0, None, [[4, 302, ['qw.rt[a-z]']]]]]], [353054897, 'Paragraph', None, 8], [920344343, 'Max_len', None, 1, [[127355787, None, 0, None, [[6, 202, ['123']]]]]], [473992973, 'Min_len', None, 1, [[1015961807, None, 0, None, [[6, 203, ['123']]]]]], [634458852, 'Re_search', None, 1, [[241461278, None, 0, None, [[4, 299, ['qw.rt[a-z]']]]]]], [799255483, 'Re_nsearch', None, 1, [[1291265633, None, 0, None, [[4, 300, ['qw.rt[a-z]']]]]]], [2121068842, 'Re_match', None, 1, [[1046017146, None, 0, None, [[4, 301, ['qw.rt[a-z]']]]]]], [456062416, 'Re_nmatch', None, 1, [[46859955, None, 0, None, [[4, 302, ['qw.rt[a-z]']]]]]]], None, None, None, None, None, None, None, 49, None, None, None, None, None, [2]], '/forms', '13_text_validation', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        grid_validation = [None, [None, [[469236292, 'RGrid_exclusive_cols', None, 7, [[1341305669, [['C1'], ['C2']], 0, ['R1'], None, None, None, None, None, None, None, [0]], [1048839025, [['C1'], ['C2']], 0, ['R2'], None, None, None, None, None, None, None, [0]]], None, None, None, [[8, 205]]], [2111609821, 'CGrid_exclusive_cols', None, 7, [[39832566, [['C1'], ['C2']], 0, ['R1'], None, None, None, None, None, None, None, [1]], [1954180210, [['C1'], ['C2']], 0, ['R2'], None, None, None, None, None, None, None, [1]]], None, None, None, [[8, 205]]]], None, None, None, [0, 0], None, None, '14_Grid_validation', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '14_Grid_validation', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        checkbox_validation = [None, [None, [[1844681314, 'CB_AtLeast2', None, 4, [[1729142119, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['', None, None, None, 1]], 0, None, [[7, 200, ['2'], 'Err_msg']], None, None, None, 0]]], [471788261, 'CB_AtMost2', None, 4, [[1122321403, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['', None, None, None, 1]], 0, None, [[7, 201, ['2'], 'Err_msg']], None, None, None, 0]]], [1634496982, 'CB_Exactly2', None, 4, [[345565332, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0], ['', None, None, None, 1]], 0, None, [[7, 204, ['2'], 'Err_msg']], None, None, None, 0]]]], None, None, None, None, None, None, '15_Checkboxes_validation', 49, None, None, None, None, None, [2]], '/forms', '15_Checkboxes_validation', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]

    class NonDeterministic(_Category):
        # data may differ when the form is reloaded
        shuffle_options = [None, [None, [[316721786, 'Radio', None, 2, [[744446594, [['Opt1', None, None, None, 0], ['Opt2', None, None, None, 0]], 0, None, None, None, None, None, 1]]], [560526143, 'CB', None, 4, [[888651629, [['Opt2', None, None, None, 0], ['Opt1', None, None, None, 0]], 0, None, None, None, None, None, 1]]], [579911729, 'DD', None, 3, [[2069524400, [['Opt2', None, None, None, 0], ['Opt1', None, None, None, 0]], 0, None, None, None, None, None, 1]]], [1857105295, 'Untitled Section', None, 8], [613738920, 'RGrid', None, 7, [[104627334, [['C1'], ['C2']], 0, ['R1'], None, None, None, None, None, None, None, [0]], [1264399636, [['C1'], ['C2']], 0, ['R2'], None, None, None, None, None, None, None, [0]]], None, None, 1], [1139293806, 'CGrid', None, 7, [[1407856401, [['C1'], ['C2']], 0, ['R2'], None, None, None, None, None, None, None, [1]], [1338634094, [['C1'], ['C2']], 0, ['R1'], None, None, None, None, None, None, None, [1]]], None, None, 1]], None, None, None, [0, 0], None, None, '16_Shuffle', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '16_Shuffle', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]

    class NotLoadable(_Category):
        # 16th element contains some data after sign-in
        file_upload = [None, [None, [[1478264753, 'Page 2', None, 8, None, -2], [1363138542, 'File', None, 13, [[1697229697, None, 0]]]], None, None, None, [0, 0], None, None, '17_file', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '17_file', None, None, None, '0', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[???]', 1, 0]

    class Settings(_Category):
        settings_email = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.1_email', 49, [None, 0, None, 2, 1], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.1_email', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_email_opt_in = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.2_email_optin', 49, [None, 0, None, 1, 1], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.2_email_optin', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_email_always = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.3_email_always', 49, [None, 0, None, 3, 1], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.3_email_always', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_submit_once = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.4_signin', 51, [None, 1, None, None, 0, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.4_signin', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 1]
        settings_edit = [None, [None, None, ['', 1, 0, 1, 0], None, None, [0, 0], None, None, '20.5_edit', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.5_edit', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_stats = [None, [None, None, ['', 1, 1, 0, 0], None, None, [0, 0], None, None, '20.6_stats', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.6_stats', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_pbar = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.7_pbar', 49, [1, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.7_pbar', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_shuffle = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.7.1_shuffle', 49, [None, None, 1, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.7.1_shuffle', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_no_resubmit_link = [None, [None, None, ['', 0, 0, 0, 0], None, None, [0, 0], None, None, '20.8_no_resub', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.8_no_resub', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_confirmation_msg = [None, [None, None, ['custom_text', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.9_cmsg', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.9_cmsg', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_disable_autosave = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, None, 51, [None, None, None, None, 0, 1], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1]], '/forms', '20.9.5_no_autosave', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_quiz = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.10_quiz', 49, [None, None, None, None, 0], None, None, None, None, [2], [[1, 1, 1, 1, 1], 1, 1]], '/forms', '20.10_quiz', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        settings_quiz_alt = [None, [None, None, ['', 1, 0, 0, 0], None, None, [0, 0], None, None, '20.11_quiz_alt', 49, [None, None, None, 2, 1], None, None, None, None, [2], [[1, 1, 0, 0, 0], 0, 1]], '/forms', '20.11_quiz_alt', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]

    class Links(_Category):
        prefilled = [None, [None, [[1908465888, 'Untitled Question', None, 0, [[1787303382, None, 0]]]], None, None, None, None, None, None, '21_prefill', 49, None, None, None, None, None, [2]], '/forms', '21_prefill', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        edit = prefilled

    class Fill(_Category):
        form_validation = [None, [None, [[1458618277, 'Short', None, 0, [[1094862044, None, 0]]], [1957636837, 'Radio_act', None, 2, [[1595443987, [['Next', None, -2, None, 0], ['Loop', None, -1, None, 0]], 0, None, None, None, None, None, 0]]], [594021868, 'Page2', None, 8]], None, None, None, [0, 0], None, None, '32_form_validate', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '32_form_validate', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]
        fill = [None, [None, [[588458215, 'Short', None, 0, [[357356599, None, 0]]], [134382366, 'Paragraph', None, 1, [[1670772026, None, 0]]], [1745531098, 'Radio', None, 2, [[1046141785, [['1', None, None, None, 0], ['2', None, None, None, 0]], 1, None, None, None, None, None, 0]]], [1511760995, 'Checkboxes', None, 4, [[906901374, [['1', None, None, None, 0], ['2', None, None, None, 0]], 1, None, None, None, None, None, 0]]], [2022251935, 'Dropdown', None, 3, [[1052461247, [['1', None, None, None, 0], ['2', None, None, None, 0]], 1, None, None, None, None, None, 0]]], [228079012, 'Scale', None, 5, [[571160326, [['1'], ['2'], ['3'], ['4'], ['5']], 1, ['', '']]]], [629090813, 'RGrid', None, 7, [[1054795295, [['1'], ['2']], 1, ['R1'], None, None, None, None, None, None, None, [0]], [214418599, [['1'], ['2']], 1, ['R2'], None, None, None, None, None, None, None, [0]]]], [967381874, 'CGrid', None, 7, [[1272718717, [['1'], ['2']], 1, ['R1'], None, None, None, None, None, None, None, [1]], [1622638484, [['1'], ['2']], 1, ['R2'], None, None, None, None, None, None, None, [1]]]], [2012468514, 'Date', None, 9, [[1407896226, None, 0, None, None, None, None, [0, 1]]]], [323888354, 'DateTime', None, 9, [[1365881642, None, 0, None, None, None, None, [1, 1]]]], [874353127, 'Time', None, 10, [[1692367778, None, 0, None, None, None, [0]]]], [784702009, 'Duration', None, 10, [[139555690, None, 0, None, None, None, [1]]]], [410318939, 'Page2', None, 8], [1414818476, 'Comment', None, 6], [490728515, 'Page3', None, 8]], None, None, None, [0, 0], None, None, '30_fill', 49, [None, None, None, None, 0], None, None, None, None, [2]], '/forms', '30_fill', None, None, None, '', None, 0, 0, None, '', 0, '0000000000000000000000000000000000000000000000000000000000', 0, '[]', 0, 0]

    _types = {}
    # generate a dynamic list?
    for cls in [Elements, NonDeterministic, NotLoadable, Settings, Links, Fill]:
        for name in cls:
            _types[name] = cls


class Draft:
    default = f'[null,null,"123456"]'
    response1 = f'[[[null,1787303382,["text_value"],0]],null,"123456",null,"{ResponseId("response1")}","123456"]'
