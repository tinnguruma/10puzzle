# サイトでも使えるようにした(Beta
https://tinnguruma.github.io/10puzzle

# 10puzzle

10パズルを階乗、平方根、括弧をつけてときます
複数回答や短回答も可能です

計算の都合上
3!は！3
(1+2)!は!(1+2)と表記しますが許してください



ver2が完成版
3は算出可能な数字を列挙します




# <<使用例>>
(2)
1>>1
2>>2
3>>3
4>>4
START?>>1
END?>>41
 >> 1 = 1*2+3-4
 >> 2 = 1*2*3-4
 >> 3 = 1+2*3-4
 >> 4 = !(1+2-3)*4
 >> 5 = (1+2)*3-4
 >> 6 = 1/2*3*4
 >> 7 = !(1+2)-3+4
 >> 8 = (1-(2-3))*4
 >> 9 = 1*2+3+4
 >> 10 = 1*2*3+4
 >> 11 = 1-(2-3*4)
 >> 12 = √(!(1+2)+3)*4
 >> 13 = !(1+2)+3+4
 >> 14 = !(1+2)*3-4
 >> 15 = 1+2+3*4
 >> 16 = !(1+2)*3-√4
 >> 17 = 1+2/3*!4
 >> 18 = !(1+2)+3*4
 >> 19 = 1-(2*3-!4)
 >> 20 = (1*2+3)*4
 >> 21 = 1+(2+3)*4
 >> 22 = !(1+2)*3+4
 >> 23 = 1*2-3+!4
 >> 24 = (1+2+3)*4
 >> 25 = 1+2*3*4
 >> 26 = !(1+2)/3+!4
 >> 27 = !(1+2)-3+!4
 >> 28 = (1+2*3)*4
 >> 29 = 1*2+3+!4
 >> 30 = !(1*2+3)/4
 >> 31 = 1+!(2+3)/4
 >> 32 = !(1+2)*!3-4
 >> 33 = !(1+2)+3+!4
 >> 34 = !(1+2)*!3-√4
 >> 35 = √(1+!(2+3))+!4
 >> 36 = (!(1+2)+3)*4
 >> 37 = 1-2*(!3-!4)
 >> 38 = !(1+2)*!3+√4
 39 NO!
 >> 40 = (1+2/3)*!4







(3)
1>>1
2>>2
3>>3
4>>4
[-1.1749972043909107e+254, -1.1100587665478609e+250, -7.849300813415672e+249, -5.5502938327393044e+249, -6.689502913449127e+198, -1.0535932642855406e+125, -8.859627990731705e+124, -7.45002941788776e+124, -3.307885441519386e+107, -1.2246891675377217e+104, -8.659860152116308e+103, -6.1234458376886085e+103, -8.32098711274139e+81, -2.308436973392414e+71, -1.2413915592536073e+61, -1.1066567523571713e+52, -9.305836959734631e+51, -7.825244940376377e+51, -3.7199332678990125e+41, -2.631308369336935e+35, -5.3050571962438214e+32, -3.7512419180464996e+32, -2.6525285981219107e+32, -8.841761993739702e+30, -2.1777738900836704e+28, -1.5399186855691705e+28, -1.0888869450418352e+28, -4.0329146112660565e+26, -1.2408968034664788e+24, -8.774465444838577e+23, -6.204484017332394e+23, -2.585201673888498e+22, -2.43290200817664e+18, -2.3032709775976908e+16, -1.936812308419817e+16, -1.6286585271694956e+16, -20922789887999.0, -87178291199.0, -11496038399.0, -11496038376.0, -1916006399.0, -1916006396.0, -958003199.0, -958003198.0, -479001623.0, -479001603.0, -479001601.0, -479001599.0, -479001598.0, -479001597.0, -479001595.0, -479001575.0, -239500799.0, -119750399.0, -19958399.0, -7257599.0, -3628801.0, -3628799.0, -3628798.0, -3628797.0, -967679.0, -967656.0, -362879.0, -161279.0, -161276.0, -80639.0, -80638.0, -40343.0, -40323.0, -40321.0, -40319.0, -40317.0, -40315.0, -40295.0, -20159.0, -17279.0, -17256.0, -10079.0, -5041.0, -5038.0, -5037.0, -2879.0, -2876.0, -2856.0, -1679.0, -1439.0, -1438.0, -743.0, -723.0, -721.0, -717.0, -715.0, -695.0, -479.0, -476.0, -359.0, -287.0, -264.0, -239.0, -238.0, -191.0, -179.0, -168.0, -145.0, -144.0, -143.0, -142.0, -141.0, -132.0, -123.0, -121.0, -120.0, -119.0, -117.0, -115.0, -96.0, -95.0, -73.0, -72.0, -70.0, -69.0, -60.0, -59.0, -53.0, -47.0, -44.0, -42.0, -41.0, -36.0, -35.0, -31.0, -30.0, -29.0, -28.0, -27.0, -25.0, -24.0, -23.0, -22.0, -21.0, -20.0, -19.0, -18.0, -17.0, -16.0, -15.0, -14.0, -13.0, -12.0, -11.0, -10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 40.0, 42.0, 43.0, 44.0, 48.0, 49.0, 52.0, 54.0, 55.0, 60.0, 61.0, 71.0, 72.0, 74.0, 75.0, 84.0, 96.0, 97.0, 116.0, 117.0, 118.0, 119.0, 120.0, 121.0, 122.0, 123.0, 124.0, 125.0, 143.0, 144.0, 145.0, 146.0, 147.0, 156.0, 168.0, 180.0, 181.0, 192.0, 193.0, 210.0, 216.0, 240.0, 241.0, 242.0, 264.0, 288.0, 289.0, 312.0, 360.0, 361.0, 432.0, 480.0, 481.0, 484.0, 696.0, 697.0, 716.0, 717.0, 718.0, 719.0, 722.0, 723.0, 724.0, 725.0, 744.0, 745.0, 1260.0, 1440.0, 1441.0, 1442.0, 1680.0, 1681.0, 2520.0, 2880.0, 2881.0, 2884.0, 2904.0, 5038.0, 5039.0, 5042.0, 5043.0, 10080.0, 10081.0, 15120.0, 17280.0, 17281.0, 17304.0, 20160.0, 20161.0, 40296.0, 40297.0, 40316.0, 40317.0, 40318.0, 40319.0, 40320.0, 40321.0, 40322.0, 40323.0, 40324.0, 40325.0, 40344.0, 40345.0, 80640.0, 80641.0, 80642.0, 90720.0, 161280.0, 161281.0, 161284.0, 181440.0, 362878.0, 362880.0, 362881.0, 362882.0, 725760.0, 967680.0, 967681.0, 967704.0, 1814400.0, 3628799.0, 3628800.0, 3628801.0, 3628802.0, 3628803.0, 7257600.0, 7257601.0, 19958400.0, 19958401.0, 119750400.0, 119750401.0, 239500800.0, 239500801.0, 259459200.0, 479001576.0, 479001577.0, 479001596.0, 479001597.0, 479001598.0, 479001599.0, 479001600.0, 479001601.0, 479001602.0, 479001603.0, 479001604.0, 479001605.0, 479001624.0, 479001625.0, 958003200.0, 958003201.0, 958003202.0, 1556755200.0, 1916006400.0, 1916006401.0, 1916006404.0, 3113510400.0, 6227020798.0, 6227020802.0, 11496038400.0, 11496038401.0, 11496038424.0, 12454041600.0, 87178291200.0, 87178291201.0, 20922789888000.0, 20922789888001.0, 266765571072000.0, 1306879060137122.0, 1600593426432000.0, 3201186852864000.0, 6402373705727995.0, 6402373705727998.0, 6402373705728002.0, 6402373705728005.0, 1.1516354887988454e+16, 1.2804747411456e+16, 1.3695331171692234e+16, 1.6286585271694956e+16, 1.936812308419817e+16, 2.3032709775976908e+16, 3.136509744329092e+16, 2.43290200817664e+18, 2.585201673888498e+22, 3.102242008666197e+23, 4.387232722419288e+23, 4.3872327224192886e+23, 6.204484017332394e+23, 8.774465444838577e+23, 1.2408968034664788e+24, 4.0329146112660565e+26, 5.444434725209176e+27, 7.69959342784585e+27, 7.699593427845852e+27, 1.0888869450418352e+28, 1.5399186855691705e+28, 2.1777738900836704e+28, 8.841761993739702e+30, 1.3262642990609553e+32, 1.8756209590232494e+32, 2.6525285981219107e+32, 3.7512419180464996e+32, 5.3050571962438214e+32, 2.631308369336935e+35, 3.7199332678990125e+41, 5.5332837617858565e+51, 6.580220418844762e+51, 7.825244940376377e+51, 9.305836959734631e+51, 1.1066567523571713e+52, 1.2413915592536073e+61, 2.308436973392414e+71, 8.32098711274139e+81, 3.0617229188443042e+103, 4.329930076058154e+103, 6.1234458376886085e+103, 8.659860152116308e+103, 1.2246891675377217e+104, 3.307885441519386e+107, 5.267966321427703e+124, 6.264703031036536e+124, 7.45002941788776e+124, 8.859627990731705e+124, 1.0535932642855406e+125, 6.689502913449127e+198, 2.7751469163696522e+249, 2.7751469163696526e+249, 3.924650406707835e+249, 5.5502938327393044e+249, 7.849300813415672e+249, 1.1100587665478609e+250, 1.1749972043909107e+254]
