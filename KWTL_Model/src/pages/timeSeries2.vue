<template>
    <div>
        <!-- 头部 -->
        <Header/>
        
        <!-- 主体 -->
        <div class="main">
          <div class="left">
             <l-map class="vue-leaflet" :zoom="zoom" :center="center">
              <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
              <!--<v-polyline-decorator :paths="[latlngs]" :patterns="patterns"></v-polyline-decorator>
             --> 
               <!-- <l-grid-layer :zIndex="zIndex"> </l-grid-layer>  --> 
                  <l-polyline v-for="(polyline,index) in poly_data"
                  :weight="weight" 
                  @mouseup="lineClick($event, index,polyline)"
                  :lat-lngs="polyline"
                  :color="color"></l-polyline>
                              
            <!-- <l-grid-layer :zIndex="zIndex_clicked"    >   </l-grid-layer> -->
            
               <l-polyline      
                  
              :weight="weight_clicked"
              :lat-lngs="poly_data_clicked"
              :color="color_clicked"></l-polyline> 
            
            </l-map>


            
                <el-row style=" margin:5px 0;">
                 <el-col :span="24">
                   <div  class="grid-content bg-purple allCenter">
                  <a class="font-show">Map kind:{{current_kind}}-Name:{{name}}-RoadID:{{id}}-Length:{{length}}Km</a>
                 </div></el-col>
                </el-row>
             <el-button plain v-on:click="drawRoad"><i style="margin-right:20px"class="el-icon-map-location"></i>Show Road Network</el-button>
            
          </div>
           <div class="right">
              <ve-line class="chart" :data="chartData" ref="chart1"></ve-line>
              <el-row>
                 <el-col :span="24">
                   <div style=" margin:5px 0px;"class="grid-content bg-purple allCenter">
                  <i style="margin-right:20px"class="el-icon-time"></i>
                  <a class="font-show">2015-04 from</a>
                  <el-input type='number' size="small" style="margin:5px; width:60px" min='1' :max='day2' v-model="day1"></el-input>
                  <a class="font-show">-</a>
                  <el-input type="number" size="small" style="margin:5px; width:60px"  min="0" :max="day1==day2?h2:23" v-model="h1"></el-input>
                  <a class="font-show">:</a>
                  <el-input type="number" size="small" style="margin:5px; width:60px"  min="0" :max="day1==day2&&h1==h2?m2:59" v-model="m1"></el-input>
                   <a class="font-show">to</a>
                  <el-input type='number' size="small" style="margin:5px; width:60px"  :min='day1' max='30'  v-model="day2"></el-input>
                  <a class="font-show">-</a>
                  <el-input type="number" size="small" style="margin:5px; width:60px"  :min="day1==day2?h1:0" max="23" v-model="h2"></el-input>
                  <a class="font-show">:</a>
                  <el-input type="number" size="small" style="margin:5px; width:60px"  :min="day1==day2&&h1==h2?m1:0" max="59" v-model="m2"></el-input>
                 </div></el-col>
                </el-row> 
                  <div class="block">
                     <span class="demonstration">预测范围</span>
                    <el-slider
                      v-model="aim"
                      show-input>
                    </el-slider>
                  </div>

              <el-button plain v-on:click="drawChart"><i style="margin-right:20px"class="el-icon-data-line"></i>Update Chart</el-button>
            </div>
           
        </div>
    </div>
</template>

<script>
import 'leaflet/dist/leaflet.css'
import Header from '@/components/Header/index.vue'
import { LMap, LTileLayer,/* LMarker ,*/ LPolyline } from 'vue2-leaflet'
import L from 'leaflet'
import roads from './1.json'
import Vue from 'vue';
import vueResource from 'vue-resource'
Vue.use(vueResource)

import VCharts from 'v-charts'
Vue.use(VCharts)
// 引入提示框组件、标题组件、工具箱组件、图例组件。
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/toolbox';
import 'echarts/lib/component/legendScroll';
// 引入v-charts折线图组件。
import VeLine from 'v-charts/lib/line';
import 'v-charts/lib/style.css';

//import Vue2LeafletPolylineDecorator from 'vue2-leaflet-polylinedecorator'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import { constants } from 'crypto';
Vue.use(ElementUI);

delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
})

Vue.component('l-map', LMap)
Vue.component('l-tile-layer', LTileLayer)
Vue.component('l-polyline', LPolyline)

export default {
  components:{
    Header,
    VeLine,
    //'v-polyline-decorator': Vue2LeafletPolylineDecorator,
  },
  data () {
    var aim=4
    var name=""
      var id=""
      var length=""
      var pinyin=""
      var poly_data_clicked=[]
      var v_data = [0]
      var map_list =[]
      var day1=1,day2=1,h1=0,m1=0,h2=0,m2=4
      //var that = this
    return {
      chartData: {
          columns: ['Time', 'real_velocity', 'linear_regression'],
          rows: []
        },
      aim:aim,
      day1:day1,
      day2:day2,
      h1:h1,
      h2:h2,
      m1:m1,
      m2:m2,
      current_kind:0,
      v_data:v_data,
      weight:6,
      weight_clicked:10,
      name:name,
      id:id,
      length:length,
      pinyin:pinyin,
      patterns:[],
      latlngs:[],
      zoom: 12,
      poly_data_clicked,
      center: L.latLng(39.913220,116.419482),
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> Haut-Gis-Org',
      poly_data:[],
      color_clicked:"#F4606C",
      color:"#19CAAD",
    }
  },
  methods: {
    num2time:function(time){
      let m = time%60
      time = Math.floor(time/60)
      let h = time % 24
      let day = Math.floor(time / 24)+1
      return day+"-"+h+":"+m
    },
    drawChart:function(){
        if(this.v_data.length<=2)
          {
            alert("请先选择一条路线")
            return
          }

        this.chartData.rows=[]
        var rows=[]
        var x = [],y = [];
        var i
        for(i = (this.day1-1)*24*60 + this.h1*60 + this.m1; i < (this.day2-1)*24*60 + this.h2*60 + this.m2; i++)
        {
            let row={}
            row['Time']=this.num2time(i)
            row['real_velocity']=this.v_data[i]
            rows.push(row)

            x.push(parseFloat(i))
            y.push(parseFloat(this.v_data[i]))
        }
        const ml = require("ml-regression");
        const SLR = ml.SLR; // 线性回归
        let regressionModel;
        regressionModel = new SLR(x, y);
        console.log(regressionModel.toString(3));
        
         let row={}
          row['Time']=this.num2time(i-1)
           row['real_velocity']=this.v_data[i]
          row['linear_regression']=this.v_data[i]
          rows.push(row)
          i++;
          for(var u = 0; u < this.aim; u++){
            let row={}
            row['Time']=this.num2time(i+u)
             row['real_velocity']=this.v_data[i+u]
            row['linear_regression']=regressionModel.predict(parseFloat(i+u))
            rows.push(row)
          }
          this.chartData.rows=rows
       
    },
    t1_change:function(){
      console.log(this.time1)
      alert(this.time1)
    },
    load_data:function(){
      this.$http.get('http://127.0.0.1:8000/load_data/?file='+this.id)
        .then(function(response){
            if(response.data.error_num != 0)
                alert(response.data.msg)
            else
                this.v_data = response.data.msg
                console.log(this.v_data)
        })
        .catch((error)=>{
            alert(error)
        }
        )
    },
    lineClick:function($event,index,polyline){
                this.name=roads["features"][index]["properties"]["Name"];
                var id = roads["features"][index]["properties"]["ID"]
                this.id=roads["features"][index]["properties"]["MapID"] + "_" + roads["features"][index]["properties"]["Kind"]+"0".repeat(4-id.length) + id;
                this.length=roads["features"][index]["properties"]["Length"];
                this.pinyin=roads["features"][index]["properties"]["PinYin"];
                this.poly_data_clicked=polyline;
                this.load_data();  
               // console.log(this.poly_data_clicked)
    },
    drawRoad: function() {
          if(this.current_kind >= 4)
            this.current_kind = 1
          else
            this.current_kind++
          var m =[]
          for(var i = 0; i < roads["features"].length; i++) {
            if(roads["features"][i]["properties"]["Kind"] == this.current_kind)
              m.push(i);
          }
          this.map_list=m;
          this.poly_data=[]
        for(var i = 0; i < this.map_list.length; i++) {
          let poly_data = [];
          let index = this.map_list[i]
          for(var u = 0; u < roads["features"][index]["geometry"]["coordinates"].length; u++){
            poly_data.push([roads["features"][index]["geometry"]["coordinates"][u][1],roads["features"][index]["geometry"]["coordinates"][u][0]])
         }
          this.poly_data.push(poly_data)
        }
        this.poly_data_clicked=[]
                //console.log(this.poly_data_clicked)
                //console.log(this.poly_data)
      },
  },
  mounted() {
    this.drawRoad()
  }
}
</script>

<style>
    #leaflet-map {
        width: 500px;
        height: 510px;
    }
    /* icon style */
    #leaflet-map .easy-button-button {
        border: none;
        border-radius: 2px;
        width: 30px;
        height: 30px;
        line-height: 30px;
        background-color: #fff;
    }
    #leaflet-map .easy-button-button .fa {
        vertical-align: 0;
        font-size: 1.3em;
    }
    @media (max-width: 768px) {
        #leaflet-map {
            height: 300px;
        }
    }
</style>

<style lang="stylus" scoped>
  .main{
      height:95%;
      height:95%;
  }
  .vue-leaflet{
      width:100%;
      height 80%;
      box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  .left{
      margin 20px 10px;
      width: 50%;
      height: 95%;
      float:left;
      text-align:center;
  }
  .right{
      width: 47%;
      height: 80%;
      float:left;
      text-align:center;
  }
  .chart{
      margin-top:20px;
      width: 100%;
      height: 50%;
      box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  .input{
    width:200px;
    margin: auto;
  }
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .font-show{
    font-family:"微软雅黑";
    font-size: 1.4em;
  }
  .allCenter{
    display:flex;
    justify-content:center;
    align-items:center;
    color:black;
  }
</style>
