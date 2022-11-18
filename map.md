## 변수    
        def save_police_norm(self):
        police_pos = pd.read_pickle('./save/police_pos.pkl')
        police = pd.pivot_table(police_pos, index="구별", aggfunc=np.sum)
        police['살인검거율'] = (police['살인 검거'] / police['살인 발생']) * 100
        police['강도검거율'] = (police['강도 검거'] / police['강도 발생']) * 100
        police['강간검거율'] = (police['강간 검거'] / police['강간 발생']) * 100
        police['절도검거율'] = (police['절도 검거'] / police['절도 발생']) * 100
        police['폭력검거율'] = (police['폭력 검거'] / police['폭력 발생']) * 100
        police.drop(columns={'살인 검거','강도 검거','강간 검거','절도 검거','폭력 검거'}, axis=1, inplace=True)
        print(police)
        for i in self.crime_rate_columns:
            police.loc[police[i]>100, 1] = 100 # 데이터값의 기간 오류로 100을 넘으면 100으로 계산
        police.rename(columns={
            '살인 발생': '살인',
            '강도 발생': '강도',
            '강간 발생': '강간',
            '절도 발생': '절도',
            '폭력 발생': '폭력'
        }, inplace=True)
        x = police[self.crime_rate_columns].values
        min_max_scalar = preprocessing.MinMaxScaler()
        """
        스케일링은 선형변환을 적용하여
        전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        """
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        """
        정규화 normalization
        많은 양의 데이터를 처리함에 있어 데이터의 범위(도메인)를 일치시키거나
        분포(스케일)를 유사하게 만드는 작업
        """
        police_norm = pd.DataFrame(x_scaled, columns=self.crime_columns, index=police.index)
        print(police_norm)
        police_norm[self.crime_rate_columns]= police[self.crime_rate_columns]
        police_norm['범죄']= np.sum(police[self.crime_rate_columns])
        police_norm['검거']= np.sum(police[self.crime_columns], axis=1)
        police_norm.to_pickle('./save/police_norm.pkl')
        print(police_norm.to_pickle('./save/police_norm.pkl'))
## 상수
    def folium_seoul(self):
        geo_data = self.ko_states

        data = None
        '''지도'''
        map = folium.Map(location=[37.5502, 126.982], zoom_start=12)
        folium.Choropleth(
            geo_data= geo_data,
            data=data,
            name="choropleth",
            columns=["State", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Crime Rate (%)'
        ).add_to(map)
        map.save("./save/crimerate.html")
## 상수2

    def create_folium_data(self):
        data = None
        crime = self.seoul_crime
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1] + '경찰서'))
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = r.gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            station_addrs.append(t[0].get('formatted_address'))
            t_loc = t[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
        police_pos['lat'] = station_lats #포지션 위치
        police_pos['lng'] = station_lngs
        temp = police_pos[self.arrest_columns] / police_pos[self.arrest_columns].max()
        police_pos['검거'] = np.sum(temp, axis=1)
        data = tuple(zip(police_norm['구별'], police_norm['범죄']))
        return data