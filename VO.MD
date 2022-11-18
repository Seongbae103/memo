# VO(Value Object) -> 개체가 될 객체
> 사용자가 입력하기 전에도 객체가 value를 가지고 있다
1. 형태
<p> 
    
    @dataclass
    class MyChoroplethVO:
        geo_data = "",
        data = object,
        name = "choropleth",
        columns = [],
        key_on = "feature.id",
        fill_color = "",
        fill_opacity = 0.0,
        line_opacity = 0.0,
        legend_name = "",
        bins = [],
        location = [],
        zoom_start = 0,
        save_path = ''
1.1 실제값이 존재할 때는 객체 / 안에 값이 들어가면 개체

2. 코딩 방식

    