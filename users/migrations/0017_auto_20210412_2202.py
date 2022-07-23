# Generated by Django 3.1.7 on 2021-04-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210412_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancersprofile',
            name='bust',
            field=models.IntegerField(blank=True, choices=[(50, '50 cm'), (51, '51 cm'), (52, '52 cm'), (53, '53 cm'), (54, '54 cm'), (55, '55 cm'), (56, '56 cm'), (57, '57 cm'), (58, '58 cm'), (59, '59 cm'), (60, '60 cm'), (61, '61 cm'), (62, '62 cm'), (63, '63 cm'), (64, '64 cm'), (65, '65 cm'), (66, '66 cm'), (67, '67 cm'), (68, '68 cm'), (69, '69 cm'), (70, '70 cm'), (71, '71 cm'), (72, '72 cm'), (73, '73 cm'), (74, '74 cm'), (75, '75 cm'), (76, '76 cm'), (77, '77 cm'), (78, '78 cm'), (79, '79 cm'), (80, '80 cm'), (81, '81 cm'), (82, '82 cm'), (83, '83 cm'), (84, '84 cm'), (85, '85 cm'), (86, '86 cm'), (87, '87 cm'), (88, '88 cm'), (89, '89 cm'), (90, '90 cm'), (91, '91 cm'), (92, '92 cm'), (93, '93 cm'), (94, '94 cm'), (95, '95 cm'), (96, '96 cm'), (97, '97 cm'), (98, '98 cm'), (99, '99 cm'), (100, '100 cm'), (101, '101 cm'), (102, '102 cm'), (103, '103 cm'), (104, '104 cm'), (105, '105 cm'), (106, '106 cm'), (107, '107 cm'), (108, '108 cm'), (109, '109 cm'), (110, '110 cm'), (111, '111 cm'), (112, '112 cm'), (113, '113 cm'), (114, '114 cm'), (115, '115 cm'), (116, '116 cm'), (117, '117 cm'), (118, '118 cm'), (119, '119 cm'), (120, '120 cm'), (121, '121 cm'), (122, '122 cm'), (123, '123 cm'), (124, '124 cm'), (125, '125 cm'), (126, '126 cm'), (127, '127 cm'), (128, '128 cm'), (129, '129 cm'), (130, '130 cm'), (131, '131 cm'), (132, '132 cm'), (133, '133 cm'), (134, '134 cm'), (135, '135 cm'), (136, '136 cm'), (137, '137 cm'), (138, '138 cm'), (139, '139 cm'), (140, '140 cm'), (141, '141 cm'), (142, '142 cm'), (143, '143 cm'), (144, '144 cm'), (145, '145 cm'), (146, '146 cm'), (147, '147 cm'), (148, '148 cm'), (149, '149 cm'), (150, '150 cm')], default='0'),
        ),
        migrations.AlterField(
            model_name='dancersprofile',
            name='hip',
            field=models.IntegerField(blank=True, choices=[(50, '50 cm'), (51, '51 cm'), (52, '52 cm'), (53, '53 cm'), (54, '54 cm'), (55, '55 cm'), (56, '56 cm'), (57, '57 cm'), (58, '58 cm'), (59, '59 cm'), (60, '60 cm'), (61, '61 cm'), (62, '62 cm'), (63, '63 cm'), (64, '64 cm'), (65, '65 cm'), (66, '66 cm'), (67, '67 cm'), (68, '68 cm'), (69, '69 cm'), (70, '70 cm'), (71, '71 cm'), (72, '72 cm'), (73, '73 cm'), (74, '74 cm'), (75, '75 cm'), (76, '76 cm'), (77, '77 cm'), (78, '78 cm'), (79, '79 cm'), (80, '80 cm'), (81, '81 cm'), (82, '82 cm'), (83, '83 cm'), (84, '84 cm'), (85, '85 cm'), (86, '86 cm'), (87, '87 cm'), (88, '88 cm'), (89, '89 cm'), (90, '90 cm'), (91, '91 cm'), (92, '92 cm'), (93, '93 cm'), (94, '94 cm'), (95, '95 cm'), (96, '96 cm'), (97, '97 cm'), (98, '98 cm'), (99, '99 cm'), (100, '100 cm'), (101, '101 cm'), (102, '102 cm'), (103, '103 cm'), (104, '104 cm'), (105, '105 cm'), (106, '106 cm'), (107, '107 cm'), (108, '108 cm'), (109, '109 cm'), (110, '110 cm'), (111, '111 cm'), (112, '112 cm'), (113, '113 cm'), (114, '114 cm'), (115, '115 cm'), (116, '116 cm'), (117, '117 cm'), (118, '118 cm'), (119, '119 cm'), (120, '120 cm'), (121, '121 cm'), (122, '122 cm'), (123, '123 cm'), (124, '124 cm'), (125, '125 cm'), (126, '126 cm'), (127, '127 cm'), (128, '128 cm'), (129, '129 cm'), (130, '130 cm'), (131, '131 cm'), (132, '132 cm'), (133, '133 cm'), (134, '134 cm'), (135, '135 cm'), (136, '136 cm'), (137, '137 cm'), (138, '138 cm'), (139, '139 cm'), (140, '140 cm'), (141, '141 cm'), (142, '142 cm'), (143, '143 cm'), (144, '144 cm'), (145, '145 cm'), (146, '146 cm'), (147, '147 cm'), (148, '148 cm'), (149, '149 cm'), (150, '150 cm')], default='0'),
        ),
        migrations.AlterField(
            model_name='dancersprofile',
            name='waist',
            field=models.IntegerField(blank=True, choices=[(50, '50 cm'), (51, '51 cm'), (52, '52 cm'), (53, '53 cm'), (54, '54 cm'), (55, '55 cm'), (56, '56 cm'), (57, '57 cm'), (58, '58 cm'), (59, '59 cm'), (60, '60 cm'), (61, '61 cm'), (62, '62 cm'), (63, '63 cm'), (64, '64 cm'), (65, '65 cm'), (66, '66 cm'), (67, '67 cm'), (68, '68 cm'), (69, '69 cm'), (70, '70 cm'), (71, '71 cm'), (72, '72 cm'), (73, '73 cm'), (74, '74 cm'), (75, '75 cm'), (76, '76 cm'), (77, '77 cm'), (78, '78 cm'), (79, '79 cm'), (80, '80 cm'), (81, '81 cm'), (82, '82 cm'), (83, '83 cm'), (84, '84 cm'), (85, '85 cm'), (86, '86 cm'), (87, '87 cm'), (88, '88 cm'), (89, '89 cm'), (90, '90 cm'), (91, '91 cm'), (92, '92 cm'), (93, '93 cm'), (94, '94 cm'), (95, '95 cm'), (96, '96 cm'), (97, '97 cm'), (98, '98 cm'), (99, '99 cm'), (100, '100 cm'), (101, '101 cm'), (102, '102 cm'), (103, '103 cm'), (104, '104 cm'), (105, '105 cm'), (106, '106 cm'), (107, '107 cm'), (108, '108 cm'), (109, '109 cm'), (110, '110 cm'), (111, '111 cm'), (112, '112 cm'), (113, '113 cm'), (114, '114 cm'), (115, '115 cm'), (116, '116 cm'), (117, '117 cm'), (118, '118 cm'), (119, '119 cm'), (120, '120 cm'), (121, '121 cm'), (122, '122 cm'), (123, '123 cm'), (124, '124 cm'), (125, '125 cm'), (126, '126 cm'), (127, '127 cm'), (128, '128 cm'), (129, '129 cm'), (130, '130 cm'), (131, '131 cm'), (132, '132 cm'), (133, '133 cm'), (134, '134 cm'), (135, '135 cm'), (136, '136 cm'), (137, '137 cm'), (138, '138 cm'), (139, '139 cm'), (140, '140 cm'), (141, '141 cm'), (142, '142 cm'), (143, '143 cm'), (144, '144 cm'), (145, '145 cm'), (146, '146 cm'), (147, '147 cm'), (148, '148 cm'), (149, '149 cm'), (150, '150 cm')], default='0'),
        ),
        migrations.AlterField(
            model_name='dancersprofile',
            name='weight',
            field=models.IntegerField(blank=True, choices=[(30, '30 kg'), (31, '31 kg'), (32, '32 kg'), (33, '33 kg'), (34, '34 kg'), (35, '35 kg'), (36, '36 kg'), (37, '37 kg'), (38, '38 kg'), (39, '39 kg'), (40, '40 kg'), (41, '41 kg'), (42, '42 kg'), (43, '43 kg'), (44, '44 kg'), (45, '45 kg'), (46, '46 kg'), (47, '47 kg'), (48, '48 kg'), (49, '49 kg'), (50, '50 kg'), (51, '51 kg'), (52, '52 kg'), (53, '53 kg'), (54, '54 kg'), (55, '55 kg'), (56, '56 kg'), (57, '57 kg'), (58, '58 kg'), (59, '59 kg'), (60, '60 kg'), (61, '61 kg'), (62, '62 kg'), (63, '63 kg'), (64, '64 kg'), (65, '65 kg'), (66, '66 kg'), (67, '67 kg'), (68, '68 kg'), (69, '69 kg'), (70, '70 kg'), (71, '71 kg'), (72, '72 kg'), (73, '73 kg'), (74, '74 kg'), (75, '75 kg'), (76, '76 kg'), (77, '77 kg'), (78, '78 kg'), (79, '79 kg'), (80, '80 kg'), (81, '81 kg'), (82, '82 kg'), (83, '83 kg'), (84, '84 kg'), (85, '85 kg'), (86, '86 kg'), (87, '87 kg'), (88, '88 kg'), (89, '89 kg'), (90, '90 kg'), (91, '91 kg'), (92, '92 kg'), (93, '93 kg'), (94, '94 kg'), (95, '95 kg'), (96, '96 kg'), (97, '97 kg'), (98, '98 kg'), (99, '99 kg'), (100, '100 kg'), (101, '101 kg'), (102, '102 kg'), (103, '103 kg'), (104, '104 kg'), (105, '105 kg'), (106, '106 kg'), (107, '107 kg'), (108, '108 kg'), (109, '109 kg'), (110, '110 kg'), (111, '111 kg'), (112, '112 kg'), (113, '113 kg'), (114, '114 kg'), (115, '115 kg'), (116, '116 kg'), (117, '117 kg'), (118, '118 kg'), (119, '119 kg'), (120, '120 kg'), (121, '121 kg'), (122, '122 kg'), (123, '123 kg'), (124, '124 kg'), (125, '125 kg'), (126, '126 kg'), (127, '127 kg'), (128, '128 kg'), (129, '129 kg'), (130, '130 kg'), (131, '131 kg'), (132, '132 kg'), (133, '133 kg'), (134, '134 kg'), (135, '135 kg'), (136, '136 kg'), (137, '137 kg'), (138, '138 kg'), (140, '140 kg'), (141, '141 kg'), (142, '142 kg'), (143, '143 kg'), (144, '144 kg'), (145, '145 kg'), (146, '146 kg'), (147, '147 kg'), (148, '148 kg'), (149, '149 kg'), (150, '150 kg')]),
        ),
    ]
