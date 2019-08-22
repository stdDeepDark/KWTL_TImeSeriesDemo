// 方式1：代码嵌入
<template>
    <div>
        <!-- 头部 -->
        <Header/>
        <!-- 主体 -->
        <div class="main">
            <!-- 添加代码 -->

            <!-- 地图 -->
            <div id="container" style="width:100%;height:100%"></div>

            <!-- 图表 -->
            <div class="chart-box">
                <!-- <ChartBox/> -->
                <div class="chart-wrap">
                    <div class="region-detail">
                        <p class="chart-title"><span>基本信息</span><cite></cite></p>
                        <div style="margin-left:20px">
                            <p><a>经度：</a><a class="figure-num">{{cur_lgt}}</a></p>
                            <p><a>纬度：</a><a class="figure-num">{{cur_lat}}</a></p>
                            <p><a>{{region_detail_tip}}：</a><a class="figure-num">{{danger_index}}</a></p>
                            <p><a>{{global_average_tip}}：</a><a class="figure-num">{{average_index}}</a></p>
                        </div>
                    </div>
                    <div class="geography-detail">
                        <p class="chart-title"><span>地理信息</span><cite></cite></p>
                        <div id="small-map"></div>
                        <div class="address-info">
                            <p class="address">{{detail_address}}</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 菜单 -->
            <div class="menu">
                <el-button-group>
                    <el-button v-for="(item,index) in menuList" :key="index" @click="clickLayer(item)" size="medium"  :class="curMapDrawActive ==item.id ? 'active':''">{{item.name}}</el-button>
                </el-button-group>
            </div>

            <!-- 时间轴选择 -->
            <div class="time-bar">
                <div style="margin:5px">
                    <a>时间选择（小时）</a>
                </div>
                <el-button-group>
                    <el-button v-for="(item,index) in timeList" :key="index" @click="clickTime(item)" size="medium"  :class="curTimeActive ==item.id ? 'active':''">{{item.name}}</el-button>
                </el-button-group>
                <!-- <el-button-group>
                    <el-button size="medium" :class="''">Play</el-button>
                </el-button-group> -->
            </div>
            
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header/index.vue'
import PeopleData from '../assets/people_data.json'
import TransportData from '../assets/transport_data.json'
import DangrData from '../assets/dangr_data.json'
import PatternData from '../assets/pattern_data.json'
import Vue from 'vue'
import vueResource from 'vue-resource'
Vue.use(vueResource)

export default {
    components:{
        Header
    },
    data(){
        var timelist = []
        var i = 0
        for (; i < 24; i++) {
            timelist.push({id:i, name:i})
        }
        return{
            menuList:[
                {id:'1',name:'人口分布'},
                {id:'2',name:'危险品分布'},
                {id:'3',name:'危险区域分布'},
                {id:'4',name:'风险模式分布'}
            ],
            timeList: timelist,
            curMapDrawActive:1,
            curTimeActive:0,
            map: null,
            gridLayer: null,
            heatmapData: PeopleData['480'],
            region_detail_tip:'人口密度指数',
            cur_lgt: 0.000,
            cur_lat: 0.000,
            danger_index: '',
            small_map:null,
            global_average_tip:'',
            average_index: 0.000,
            detail_address: '', 
            patternGroup: null,
            patternData: PatternData['data'],
            ggeocoder: null
        }
       
    },
    methods:{
        clickLayer(obj){
            this.curMapDrawActive = obj.id
            // if (obj.id == '1') this.peopleHeat();
            // if (obj.id == '2') this.transportHeat();
            // if (obj.id == '3') this.dangrHeat();
            if (obj.id == '4') {
                this.gridLayer.setData([])
                this.gridLayer.render()
            }
            this.renderHeatMap()
        },
        peopleHeat(){
            let testData = PeopleData['480'];
            this.gridLayer.setData(testData, {
                lnglat: 'lnglat',
                value: 'value'
            })
            this.gridLayer.render()
        },
        transportHeat(){
            let testData = TransportData['480'];
            this.gridLayer.setData(testData, {
                lnglat: 'lnglat',
                value: 'value'
            })
            this.gridLayer.render()
        },
        dangrHeat(){
            let testData = DangrData['480'];
            this.gridLayer.setData(testData, {
                lnglat: 'lnglat',
                value: 'value'
            })
            this.gridLayer.render()
        },
        clickTime(obj){
            this.curTimeActive = obj.id
            this.renderHeatMap()
        },
        load_data: function(type){
            this.$http.get('http://115.28.163.137:8000/heatmap_data/?type='+type+'&time='+this.curTimeActive)
                .then(function(response) {
                    console.log(response.data.data)
                    if (type != 'pattern') {
                        this.patternGroup.hide()
                        this.heatmapData = response.data.data
                        this.gridLayer.setData(this.heatmapData, {
                            lnglat: 'lnglat',
                            value: 'value'
                        })
                        var cnt = this.heatmapData.length, total = 0.0
                        for (var i = 0; i < cnt; i++) {
                            total += this.heatmapData[i].value
                        }
                        this.average_index = total / cnt
                        this.average_index = this.average_index.toFixed(4);
                        this.gridLayer.render()
                    }
                    else {
                        this.patternData = response.data.data
                        this.patternGroup.clearOverlays()
                        var that = this
                        var patternClickHandler = function(e) {
                            var extdata = e.target.getExtData()
                            that.danger_index = extdata.value
                            that.danger_index = that.danger_index.toFixed(4)
                            that.average_index = extdata.len

                            that.cur_lgt = e.lnglat.getLng()
                            that.cur_lat = e.lnglat.getLat()
                            // that.danger_index = 0.01
                            that.small_map.setCenter(e.lnglat)
                            that.ggeocoder.getAddress(e.lnglat, function(status, result) {
                                if (status === 'complete' && result.info === 'OK') {
                                    var address = result.regeocode.formattedAddress;
                                    that.detail_address = address
                                }
                            })
                        }
                        for (i = 0; i < this.patternData.length; i++) {
                            var bounds = this.patternData[i].bounds
                            var extdata = {}
                            extdata['value'] = this.patternData[i].value
                            extdata['len'] = this.patternData[i].len
                            for (var j = 0; j < bounds.length; j++) {
                                var SW = new AMap.LngLat(bounds[j].SW[0], bounds[j].SW[1])
                                var NE = new AMap.LngLat(bounds[j].NE[0], bounds[j].NE[1])
                                var boundsj = new AMap.Bounds(SW, NE)
                                var rect = new AMap.Rectangle({'bounds': boundsj, 'extData': extdata, 'fillColor': '#f66356', 'strokeColor': '#f97b57'})
                                rect.on('click', patternClickHandler)
                                this.patternGroup.addOverlay(rect)
                            }
                        }
                        this.patternGroup.show()
                    }
                })
                .catch((error)=>{
                    console.log(error)
                    if (type != 'pattern') {
                        this.patternGroup.hide()
                        if (type == 'people') this.heatmapData = PeopleData['480']
                        if (type == 'danger') this.heatmapData = DangrData['480']
                        if (type == 'transport') this.heatmapData = TransportData['480']
                        this.gridLayer.setData(this.heatmapData, {
                            lnglat: 'lnglat',
                            value: 'value'
                        })
                        var cnt = this.heatmapData.length, total = 0.0
                        for (var i = 0; i < cnt; i++) {
                            total += this.heatmapData[i].value
                        }
                        this.average_index = total / cnt
                        this.average_index = this.average_index.toFixed(4);
                        this.gridLayer.render()
                    }
                    else {
                        this.patternData = PatternData['data']
                        this.patternGroup.clearOverlays()
                        var that = this
                        var patternClickHandler = function(e) {
                            var extdata = e.target.getExtData()
                            that.danger_index = extdata.value
                            that.danger_index = that.danger_index.toFixed(4)
                            that.average_index = extdata.len

                            that.cur_lgt = e.lnglat.getLng()
                            that.cur_lat = e.lnglat.getLat()
                            // that.danger_index = 0.01
                            that.small_map.setCenter(e.lnglat)
                            that.ggeocoder.getAddress(e.lnglat, function(status, result) {
                                if (status === 'complete' && result.info === 'OK') {
                                    var address = result.regeocode.formattedAddress;
                                    that.detail_address = address
                                }
                            })
                        }
                        for (i = 0; i < this.patternData.length; i++) {
                            var bounds = this.patternData[i].bounds
                            var extdata = {}
                            extdata['value'] = this.patternData[i].value
                            extdata['len'] = this.patternData[i].len
                            for (var j = 0; j < bounds.length; j++) {
                                var SW = new AMap.LngLat(bounds[j].SW[0], bounds[j].SW[1])
                                var NE = new AMap.LngLat(bounds[j].NE[0], bounds[j].NE[1])
                                var boundsj = new AMap.Bounds(SW, NE)
                                var rect = new AMap.Rectangle({'bounds': boundsj, 'extData': extdata, 'fillColor': '#f66356', 'strokeColor': '#f97b57'})
                                rect.on('click', patternClickHandler)
                                this.patternGroup.addOverlay(rect)
                            }
                        }
                        this.patternGroup.show()

                        
                    }
                })
        },
        renderHeatMap() {
            var type = ''
            if (this.curMapDrawActive == '1') {
                type = 'people'
                this.region_detail_tip = '人口密度指数'
                this.global_average_tip = '全市平均水平'
            }
            if (this.curMapDrawActive == '2') {
                type = 'transport'
                this.region_detail_tip = '危险品密度指数'
                this.global_average_tip = '全市平均水平'
            }
            if (this.curMapDrawActive == '3') {
                type = 'danger'
                this.region_detail_tip = '区域危险指数'
                this.global_average_tip = '全市平均水平'
            }
            if (this.curMapDrawActive == '4') {
                type = 'pattern'
                this.region_detail_tip = '风险模式评分'
                this.global_average_tip = '风险模式大小'
                this.danger_index = ''
                this.average_index = ''
            }
            this.load_data(type)
        }
    },
    mounted(){
        this.map = new AMap.Map('container', {
          mapStyle: 'amap://styles/dark',
          center:[116.5, 39.9],
          zoom:11
        }); 
        this.gridLayer = new Loca.GridLayer({
            map: this.map
        });
        this.gridLayer.setOptions({
            unit: 'meter',
            mode: 'max',
            style: {
                // color: ['#ecda9a', '#efc47e', '#f3ad6a', '#f7945d', '#f97b57', '#f66356', '#ee4d5a'],
                color: ['#CCFF33', '#D3E539', '#DACB3F', '#E1B145', '#E8974A', '#EF7D50', '#F66356'],
                radius: 500,
                opacity: [0.6, 0.8],
                gap: 0
            }
        });
        this.patternGroup = new AMap.OverlayGroup();
        this.patternGroup.setMap(this.map);
        var geocoder;
        AMap.plugin('AMap.Geocoder', function() {
            geocoder = new AMap.Geocoder({
                // city 指定进行编码查询的城市，支持传入城市名、adcode 和 citycode
                city: '010',
                radius: 300
            })
        })
        this.ggeocoder = geocoder
        var that = this;
        var clickHandler = function(e) {
            that.cur_lgt = e.lnglat.getLng()
            that.cur_lat = e.lnglat.getLat()
            // that.danger_index = 0.01
            that.small_map.setCenter(e.lnglat)
            geocoder.getAddress(e.lnglat, function(status, result) {
                if (status === 'complete' && result.info === 'OK') {
                    var address = result.regeocode.formattedAddress;
                    that.detail_address = address
                }
            })

            if (that.curMapDrawActive != '4') {
                var min_dist = 1000000, cur_index = 0
                for (var i = 0, l = that.heatmapData.length; i < l; i++) {
                    var pntlnglat = that.heatmapData[i].lnglat
                    var pntlng = pntlnglat[0], pntlat = pntlnglat[1]
                    var difflng = pntlng - that.cur_lgt, difflat = pntlat - that.cur_lat
                    var nowdist = difflng * difflng + difflat * difflat
                    if (nowdist < min_dist) {
                        min_dist = nowdist
                        cur_index = that.heatmapData[i].value.toFixed(4)
                    }
                }
                that.danger_index = cur_index
            }
            
            
            console.log('您在[ '+e.lnglat.getLng()+','+e.lnglat.getLat()+' ]的位置点击了地图！');
        };

        // 绑定事件
        this.map.on('click', clickHandler);
        this.renderHeatMap();

        this.small_map = new AMap.Map('small-map', {
          mapStyle: 'amap://styles/light',
          center:[116.3975, 39.9082],
          zoom:14
        }); 
    }
}
</script>

<style lang="stylus" scoped>
.main
    height 100%
.chart-box
    height 100%
.chart-wrap
    width 31%
    height 100%
    position absolute
    top 35px
    right 0
    z-index 20
    min-width 480px

.region-detail
    width 100%
    height 180px
    margin-top 15px
    background: linear-gradient(to right, rgba(62,73,103,0.7), rgba(48,58,88,1));
    box-shadow 8px 8px 8px rgba(0, 0,0, 0.5)
    margin-bottom 10px


.geography-detail
    width 100%
    height 460px
    margin-top 15px
    background: linear-gradient(to right, rgba(62,73,103,0.7), rgba(48,58,88,1));
    box-shadow 8px 8px 8px rgba(0, 0,0, 0.5)
    margin-bottom 10px


.menu
    position absolute
    left 10px
    top 100px

    .el-button
        background: #303a58;
        border: 1px solid #303a58;
        color: #c0c4cc; 

    .el-button:hover,.el-button.active
        color #13ffd7
.time-bar
    position absolute
    left 10px
    bottom 10px
    z-index 50

    .el-button
        background: #303a58;
        border: 1px solid #303a58;
        color: #c0c4cc; 

    .el-button:hover,.el-button.active
        color #13ffd7

.chart-title
  position relative
  height 30px
  line-height 30px
  margin-left 10px

.chart-title
  span 
    display inline-block
    font-size 16px
    color #fff

.chart-title
  cite
    position absolute
    left: -10px;
    top: 0;
    width: 5px;
    height: 30px;
    background #13ffd7

.figure-num
    color rgb(0,255,188)
    font-size 25px
    font-weight bold

.address
    color rgb(0,255,188)
    font-size 20px
    font-weight bold
    margin 10px

#small-map
    width 90%
    height 75%
    margin-left 25px
    margin-top 10px
</style>
