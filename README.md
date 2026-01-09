# Custom Marching Cubes Configuration Generator

This is a custom asymmetric marching cubes generator that can be used for volumetric data imaging.
The purpose of this project was to find a way to algorithmically generate vertices, edges and ordered triangles to be used as a substitute for generic MC lookup tables.

The produced polygons should be airtight as the idea is to always prefer to fill "solid" edges not to cross any empty/"air" nodes.

In all probability the available marching cubes lookup-tables (Marching Cubes 33) are superior to the one generated here, but out of curiosity this had to be done.

# All Configurations, Visualized
![image](output/all_cube_configurations.png "All configurations")

Configuration 0       | Complement 255
|-----------|----------|
|![Configuration: 0](output/configuration0.png) | ![Configuration: 255](output/configuration255.png)|)

Configuration 1       | Complement 254
|-----------|----------|
|![Configuration: 1](output/configuration1.png) | ![Configuration: 254](output/configuration254.png)|)

Configuration 2       | Complement 253
|-----------|----------|
|![Configuration: 2](output/configuration2.png) | ![Configuration: 253](output/configuration253.png)|)

Configuration 3       | Complement 252
|-----------|----------|
|![Configuration: 3](output/configuration3.png) | ![Configuration: 252](output/configuration252.png)|)

Configuration 4       | Complement 251
|-----------|----------|
|![Configuration: 4](output/configuration4.png) | ![Configuration: 251](output/configuration251.png)|)

Configuration 5       | Complement 250
|-----------|----------|
|![Configuration: 5](output/configuration5.png) | ![Configuration: 250](output/configuration250.png)|)

Configuration 6       | Complement 249
|-----------|----------|
|![Configuration: 6](output/configuration6.png) | ![Configuration: 249](output/configuration249.png)|)

Configuration 7       | Complement 248
|-----------|----------|
|![Configuration: 7](output/configuration7.png) | ![Configuration: 248](output/configuration248.png)|)

Configuration 8       | Complement 247
|-----------|----------|
|![Configuration: 8](output/configuration8.png) | ![Configuration: 247](output/configuration247.png)|)

Configuration 9       | Complement 246
|-----------|----------|
|![Configuration: 9](output/configuration9.png) | ![Configuration: 246](output/configuration246.png)|)

Configuration 10       | Complement 245
|-----------|----------|
|![Configuration: 10](output/configuration10.png) | ![Configuration: 245](output/configuration245.png)|)

Configuration 11       | Complement 244
|-----------|----------|
|![Configuration: 11](output/configuration11.png) | ![Configuration: 244](output/configuration244.png)|)

Configuration 12       | Complement 243
|-----------|----------|
|![Configuration: 12](output/configuration12.png) | ![Configuration: 243](output/configuration243.png)|)

Configuration 13       | Complement 242
|-----------|----------|
|![Configuration: 13](output/configuration13.png) | ![Configuration: 242](output/configuration242.png)|)

Configuration 14       | Complement 241
|-----------|----------|
|![Configuration: 14](output/configuration14.png) | ![Configuration: 241](output/configuration241.png)|)

Configuration 15       | Complement 240
|-----------|----------|
|![Configuration: 15](output/configuration15.png) | ![Configuration: 240](output/configuration240.png)|)

Configuration 16       | Complement 239
|-----------|----------|
|![Configuration: 16](output/configuration16.png) | ![Configuration: 239](output/configuration239.png)|)

Configuration 17       | Complement 238
|-----------|----------|
|![Configuration: 17](output/configuration17.png) | ![Configuration: 238](output/configuration238.png)|)

Configuration 18       | Complement 237
|-----------|----------|
|![Configuration: 18](output/configuration18.png) | ![Configuration: 237](output/configuration237.png)|)

Configuration 19       | Complement 236
|-----------|----------|
|![Configuration: 19](output/configuration19.png) | ![Configuration: 236](output/configuration236.png)|)

Configuration 20       | Complement 235
|-----------|----------|
|![Configuration: 20](output/configuration20.png) | ![Configuration: 235](output/configuration235.png)|)

Configuration 21       | Complement 234
|-----------|----------|
|![Configuration: 21](output/configuration21.png) | ![Configuration: 234](output/configuration234.png)|)

Configuration 22       | Complement 233
|-----------|----------|
|![Configuration: 22](output/configuration22.png) | ![Configuration: 233](output/configuration233.png)|)

Configuration 23       | Complement 232
|-----------|----------|
|![Configuration: 23](output/configuration23.png) | ![Configuration: 232](output/configuration232.png)|)

Configuration 24       | Complement 231
|-----------|----------|
|![Configuration: 24](output/configuration24.png) | ![Configuration: 231](output/configuration231.png)|)

Configuration 25       | Complement 230
|-----------|----------|
|![Configuration: 25](output/configuration25.png) | ![Configuration: 230](output/configuration230.png)|)

Configuration 26       | Complement 229
|-----------|----------|
|![Configuration: 26](output/configuration26.png) | ![Configuration: 229](output/configuration229.png)|)

Configuration 27       | Complement 228
|-----------|----------|
|![Configuration: 27](output/configuration27.png) | ![Configuration: 228](output/configuration228.png)|)

Configuration 28       | Complement 227
|-----------|----------|
|![Configuration: 28](output/configuration28.png) | ![Configuration: 227](output/configuration227.png)|)

Configuration 29       | Complement 226
|-----------|----------|
|![Configuration: 29](output/configuration29.png) | ![Configuration: 226](output/configuration226.png)|)

Configuration 30       | Complement 225
|-----------|----------|
|![Configuration: 30](output/configuration30.png) | ![Configuration: 225](output/configuration225.png)|)

Configuration 31       | Complement 224
|-----------|----------|
|![Configuration: 31](output/configuration31.png) | ![Configuration: 224](output/configuration224.png)|)

Configuration 32       | Complement 223
|-----------|----------|
|![Configuration: 32](output/configuration32.png) | ![Configuration: 223](output/configuration223.png)|)

Configuration 33       | Complement 222
|-----------|----------|
|![Configuration: 33](output/configuration33.png) | ![Configuration: 222](output/configuration222.png)|)

Configuration 34       | Complement 221
|-----------|----------|
|![Configuration: 34](output/configuration34.png) | ![Configuration: 221](output/configuration221.png)|)

Configuration 35       | Complement 220
|-----------|----------|
|![Configuration: 35](output/configuration35.png) | ![Configuration: 220](output/configuration220.png)|)

Configuration 36       | Complement 219
|-----------|----------|
|![Configuration: 36](output/configuration36.png) | ![Configuration: 219](output/configuration219.png)|)

Configuration 37       | Complement 218
|-----------|----------|
|![Configuration: 37](output/configuration37.png) | ![Configuration: 218](output/configuration218.png)|)

Configuration 38       | Complement 217
|-----------|----------|
|![Configuration: 38](output/configuration38.png) | ![Configuration: 217](output/configuration217.png)|)

Configuration 39       | Complement 216
|-----------|----------|
|![Configuration: 39](output/configuration39.png) | ![Configuration: 216](output/configuration216.png)|)

Configuration 40       | Complement 215
|-----------|----------|
|![Configuration: 40](output/configuration40.png) | ![Configuration: 215](output/configuration215.png)|)

Configuration 41       | Complement 214
|-----------|----------|
|![Configuration: 41](output/configuration41.png) | ![Configuration: 214](output/configuration214.png)|)

Configuration 42       | Complement 213
|-----------|----------|
|![Configuration: 42](output/configuration42.png) | ![Configuration: 213](output/configuration213.png)|)

Configuration 43       | Complement 212
|-----------|----------|
|![Configuration: 43](output/configuration43.png) | ![Configuration: 212](output/configuration212.png)|)

Configuration 44       | Complement 211
|-----------|----------|
|![Configuration: 44](output/configuration44.png) | ![Configuration: 211](output/configuration211.png)|)

Configuration 45       | Complement 210
|-----------|----------|
|![Configuration: 45](output/configuration45.png) | ![Configuration: 210](output/configuration210.png)|)

Configuration 46       | Complement 209
|-----------|----------|
|![Configuration: 46](output/configuration46.png) | ![Configuration: 209](output/configuration209.png)|)

Configuration 47       | Complement 208
|-----------|----------|
|![Configuration: 47](output/configuration47.png) | ![Configuration: 208](output/configuration208.png)|)

Configuration 48       | Complement 207
|-----------|----------|
|![Configuration: 48](output/configuration48.png) | ![Configuration: 207](output/configuration207.png)|)

Configuration 49       | Complement 206
|-----------|----------|
|![Configuration: 49](output/configuration49.png) | ![Configuration: 206](output/configuration206.png)|)

Configuration 50       | Complement 205
|-----------|----------|
|![Configuration: 50](output/configuration50.png) | ![Configuration: 205](output/configuration205.png)|)

Configuration 51       | Complement 204
|-----------|----------|
|![Configuration: 51](output/configuration51.png) | ![Configuration: 204](output/configuration204.png)|)

Configuration 52       | Complement 203
|-----------|----------|
|![Configuration: 52](output/configuration52.png) | ![Configuration: 203](output/configuration203.png)|)

Configuration 53       | Complement 202
|-----------|----------|
|![Configuration: 53](output/configuration53.png) | ![Configuration: 202](output/configuration202.png)|)

Configuration 54       | Complement 201
|-----------|----------|
|![Configuration: 54](output/configuration54.png) | ![Configuration: 201](output/configuration201.png)|)

Configuration 55       | Complement 200
|-----------|----------|
|![Configuration: 55](output/configuration55.png) | ![Configuration: 200](output/configuration200.png)|)

Configuration 56       | Complement 199
|-----------|----------|
|![Configuration: 56](output/configuration56.png) | ![Configuration: 199](output/configuration199.png)|)

Configuration 57       | Complement 198
|-----------|----------|
|![Configuration: 57](output/configuration57.png) | ![Configuration: 198](output/configuration198.png)|)

Configuration 58       | Complement 197
|-----------|----------|
|![Configuration: 58](output/configuration58.png) | ![Configuration: 197](output/configuration197.png)|)

Configuration 59       | Complement 196
|-----------|----------|
|![Configuration: 59](output/configuration59.png) | ![Configuration: 196](output/configuration196.png)|)

Configuration 60       | Complement 195
|-----------|----------|
|![Configuration: 60](output/configuration60.png) | ![Configuration: 195](output/configuration195.png)|)

Configuration 61       | Complement 194
|-----------|----------|
|![Configuration: 61](output/configuration61.png) | ![Configuration: 194](output/configuration194.png)|)

Configuration 62       | Complement 193
|-----------|----------|
|![Configuration: 62](output/configuration62.png) | ![Configuration: 193](output/configuration193.png)|)

Configuration 63       | Complement 192
|-----------|----------|
|![Configuration: 63](output/configuration63.png) | ![Configuration: 192](output/configuration192.png)|)

Configuration 64       | Complement 191
|-----------|----------|
|![Configuration: 64](output/configuration64.png) | ![Configuration: 191](output/configuration191.png)|)

Configuration 65       | Complement 190
|-----------|----------|
|![Configuration: 65](output/configuration65.png) | ![Configuration: 190](output/configuration190.png)|)

Configuration 66       | Complement 189
|-----------|----------|
|![Configuration: 66](output/configuration66.png) | ![Configuration: 189](output/configuration189.png)|)

Configuration 67       | Complement 188
|-----------|----------|
|![Configuration: 67](output/configuration67.png) | ![Configuration: 188](output/configuration188.png)|)

Configuration 68       | Complement 187
|-----------|----------|
|![Configuration: 68](output/configuration68.png) | ![Configuration: 187](output/configuration187.png)|)

Configuration 69       | Complement 186
|-----------|----------|
|![Configuration: 69](output/configuration69.png) | ![Configuration: 186](output/configuration186.png)|)

Configuration 70       | Complement 185
|-----------|----------|
|![Configuration: 70](output/configuration70.png) | ![Configuration: 185](output/configuration185.png)|)

Configuration 71       | Complement 184
|-----------|----------|
|![Configuration: 71](output/configuration71.png) | ![Configuration: 184](output/configuration184.png)|)

Configuration 72       | Complement 183
|-----------|----------|
|![Configuration: 72](output/configuration72.png) | ![Configuration: 183](output/configuration183.png)|)

Configuration 73       | Complement 182
|-----------|----------|
|![Configuration: 73](output/configuration73.png) | ![Configuration: 182](output/configuration182.png)|)

Configuration 74       | Complement 181
|-----------|----------|
|![Configuration: 74](output/configuration74.png) | ![Configuration: 181](output/configuration181.png)|)

Configuration 75       | Complement 180
|-----------|----------|
|![Configuration: 75](output/configuration75.png) | ![Configuration: 180](output/configuration180.png)|)

Configuration 76       | Complement 179
|-----------|----------|
|![Configuration: 76](output/configuration76.png) | ![Configuration: 179](output/configuration179.png)|)

Configuration 77       | Complement 178
|-----------|----------|
|![Configuration: 77](output/configuration77.png) | ![Configuration: 178](output/configuration178.png)|)

Configuration 78       | Complement 177
|-----------|----------|
|![Configuration: 78](output/configuration78.png) | ![Configuration: 177](output/configuration177.png)|)

Configuration 79       | Complement 176
|-----------|----------|
|![Configuration: 79](output/configuration79.png) | ![Configuration: 176](output/configuration176.png)|)

Configuration 80       | Complement 175
|-----------|----------|
|![Configuration: 80](output/configuration80.png) | ![Configuration: 175](output/configuration175.png)|)

Configuration 81       | Complement 174
|-----------|----------|
|![Configuration: 81](output/configuration81.png) | ![Configuration: 174](output/configuration174.png)|)

Configuration 82       | Complement 173
|-----------|----------|
|![Configuration: 82](output/configuration82.png) | ![Configuration: 173](output/configuration173.png)|)

Configuration 83       | Complement 172
|-----------|----------|
|![Configuration: 83](output/configuration83.png) | ![Configuration: 172](output/configuration172.png)|)

Configuration 84       | Complement 171
|-----------|----------|
|![Configuration: 84](output/configuration84.png) | ![Configuration: 171](output/configuration171.png)|)

Configuration 85       | Complement 170
|-----------|----------|
|![Configuration: 85](output/configuration85.png) | ![Configuration: 170](output/configuration170.png)|)

Configuration 86       | Complement 169
|-----------|----------|
|![Configuration: 86](output/configuration86.png) | ![Configuration: 169](output/configuration169.png)|)

Configuration 87       | Complement 168
|-----------|----------|
|![Configuration: 87](output/configuration87.png) | ![Configuration: 168](output/configuration168.png)|)

Configuration 88       | Complement 167
|-----------|----------|
|![Configuration: 88](output/configuration88.png) | ![Configuration: 167](output/configuration167.png)|)

Configuration 89       | Complement 166
|-----------|----------|
|![Configuration: 89](output/configuration89.png) | ![Configuration: 166](output/configuration166.png)|)

Configuration 90       | Complement 165
|-----------|----------|
|![Configuration: 90](output/configuration90.png) | ![Configuration: 165](output/configuration165.png)|)

Configuration 91       | Complement 164
|-----------|----------|
|![Configuration: 91](output/configuration91.png) | ![Configuration: 164](output/configuration164.png)|)

Configuration 92       | Complement 163
|-----------|----------|
|![Configuration: 92](output/configuration92.png) | ![Configuration: 163](output/configuration163.png)|)

Configuration 93       | Complement 162
|-----------|----------|
|![Configuration: 93](output/configuration93.png) | ![Configuration: 162](output/configuration162.png)|)

Configuration 94       | Complement 161
|-----------|----------|
|![Configuration: 94](output/configuration94.png) | ![Configuration: 161](output/configuration161.png)|)

Configuration 95       | Complement 160
|-----------|----------|
|![Configuration: 95](output/configuration95.png) | ![Configuration: 160](output/configuration160.png)|)

Configuration 96       | Complement 159
|-----------|----------|
|![Configuration: 96](output/configuration96.png) | ![Configuration: 159](output/configuration159.png)|)

Configuration 97       | Complement 158
|-----------|----------|
|![Configuration: 97](output/configuration97.png) | ![Configuration: 158](output/configuration158.png)|)

Configuration 98       | Complement 157
|-----------|----------|
|![Configuration: 98](output/configuration98.png) | ![Configuration: 157](output/configuration157.png)|)

Configuration 99       | Complement 156
|-----------|----------|
|![Configuration: 99](output/configuration99.png) | ![Configuration: 156](output/configuration156.png)|)

Configuration 100       | Complement 155
|-----------|----------|
|![Configuration: 100](output/configuration100.png) | ![Configuration: 155](output/configuration155.png)|)

Configuration 101       | Complement 154
|-----------|----------|
|![Configuration: 101](output/configuration101.png) | ![Configuration: 154](output/configuration154.png)|)

Configuration 102       | Complement 153
|-----------|----------|
|![Configuration: 102](output/configuration102.png) | ![Configuration: 153](output/configuration153.png)|)

Configuration 103       | Complement 152
|-----------|----------|
|![Configuration: 103](output/configuration103.png) | ![Configuration: 152](output/configuration152.png)|)

Configuration 104       | Complement 151
|-----------|----------|
|![Configuration: 104](output/configuration104.png) | ![Configuration: 151](output/configuration151.png)|)

Configuration 105       | Complement 150
|-----------|----------|
|![Configuration: 105](output/configuration105.png) | ![Configuration: 150](output/configuration150.png)|)

Configuration 106       | Complement 149
|-----------|----------|
|![Configuration: 106](output/configuration106.png) | ![Configuration: 149](output/configuration149.png)|)

Configuration 107       | Complement 148
|-----------|----------|
|![Configuration: 107](output/configuration107.png) | ![Configuration: 148](output/configuration148.png)|)

Configuration 108       | Complement 147
|-----------|----------|
|![Configuration: 108](output/configuration108.png) | ![Configuration: 147](output/configuration147.png)|)

Configuration 109       | Complement 146
|-----------|----------|
|![Configuration: 109](output/configuration109.png) | ![Configuration: 146](output/configuration146.png)|)

Configuration 110       | Complement 145
|-----------|----------|
|![Configuration: 110](output/configuration110.png) | ![Configuration: 145](output/configuration145.png)|)

Configuration 111       | Complement 144
|-----------|----------|
|![Configuration: 111](output/configuration111.png) | ![Configuration: 144](output/configuration144.png)|)

Configuration 112       | Complement 143
|-----------|----------|
|![Configuration: 112](output/configuration112.png) | ![Configuration: 143](output/configuration143.png)|)

Configuration 113       | Complement 142
|-----------|----------|
|![Configuration: 113](output/configuration113.png) | ![Configuration: 142](output/configuration142.png)|)

Configuration 114       | Complement 141
|-----------|----------|
|![Configuration: 114](output/configuration114.png) | ![Configuration: 141](output/configuration141.png)|)

Configuration 115       | Complement 140
|-----------|----------|
|![Configuration: 115](output/configuration115.png) | ![Configuration: 140](output/configuration140.png)|)

Configuration 116       | Complement 139
|-----------|----------|
|![Configuration: 116](output/configuration116.png) | ![Configuration: 139](output/configuration139.png)|)

Configuration 117       | Complement 138
|-----------|----------|
|![Configuration: 117](output/configuration117.png) | ![Configuration: 138](output/configuration138.png)|)

Configuration 118       | Complement 137
|-----------|----------|
|![Configuration: 118](output/configuration118.png) | ![Configuration: 137](output/configuration137.png)|)

Configuration 119       | Complement 136
|-----------|----------|
|![Configuration: 119](output/configuration119.png) | ![Configuration: 136](output/configuration136.png)|)

Configuration 120       | Complement 135
|-----------|----------|
|![Configuration: 120](output/configuration120.png) | ![Configuration: 135](output/configuration135.png)|)

Configuration 121       | Complement 134
|-----------|----------|
|![Configuration: 121](output/configuration121.png) | ![Configuration: 134](output/configuration134.png)|)

Configuration 122       | Complement 133
|-----------|----------|
|![Configuration: 122](output/configuration122.png) | ![Configuration: 133](output/configuration133.png)|)

Configuration 123       | Complement 132
|-----------|----------|
|![Configuration: 123](output/configuration123.png) | ![Configuration: 132](output/configuration132.png)|)

Configuration 124       | Complement 131
|-----------|----------|
|![Configuration: 124](output/configuration124.png) | ![Configuration: 131](output/configuration131.png)|)

Configuration 125       | Complement 130
|-----------|----------|
|![Configuration: 125](output/configuration125.png) | ![Configuration: 130](output/configuration130.png)|)

Configuration 126       | Complement 129
|-----------|----------|
|![Configuration: 126](output/configuration126.png) | ![Configuration: 129](output/configuration129.png)|)

Configuration 127       | Complement 128
|-----------|----------|
|![Configuration: 127](output/configuration127.png) | ![Configuration: 128](output/configuration128.png)|)

