<template>
    <div>
        <!-- 头部 -->
        <Header/>
        
        <!-- 主体 -->
        <div class="main">
         <!-- <div id= "container" style="width:200px; height=200px;"></div>
         -->
          
             <l-map style="position:absolute; z-index:0; width:100%;height:100%;" :zoom="zoom" :center="center">
              <l-tile-layer style="position:absolute;" :url="url" :attribution="attribution"></l-tile-layer>

                  <l-polyline v-for="(polyline,Pindex) in poly_data"
                  :weight="weight" 
                  @mouseup="lineClick($event,Pindex,polyline)"
                  :lat-lngs="polyline.line"
                  :color="polyline.color"></l-polyline>
                <!--                    
               <l-polyline  
               style="position:absolute; z-index:5"              
              :weight="weight_clicked"
              :lat-lngs="poly_data_clicked"
              :color="color_clicked"></l-polyline> 
              -->
            </l-map>
            <div class="menu ">
              <div style="margin:5px">
                    <a class="font-bg ">Map kind:</a>
                    <a class="font-show">{{current_kind}}</a>
              </div>
              <div style="margin:5px">
                    <a class="font-bg">Name:</a>
                    <a class="font-show">{{name}}</a>
              </div>
              <div style="margin:5px">
                    <a class="font-bg ">Length:</a>
                    <a class="font-show">{{length}}Km</a>
              </div>
              <el-button class="button" style="margin:10px 0" @click="drawRoad"><i style="margin-right:20px"class="el-icon-map-location"></i>Show Road Network</el-button>
                   
            </div>

           <div class="right">

              <ve-line class="chart" :data="chartData" :extend="chartExtend"></ve-line>
              
                   <div style=" margin:5px 0px;"class="block-bg allCenter">
                    <i style="margin-right:2px"class="el-icon-time"></i>
                    <a class="font-show">2015-04 from</a>
                    <el-input type='number' size="small" style="margin:5px; width:60px" min='1' :max='h1==23&&h2==0||h1+1>h2?day2-1:day2' v-model="day1"></el-input>
                    <a class="font-show">-</a>
                    <el-input type="number" size="small" style="margin:5px; width:60px"  min="0" :max="day1==day2?h2-1:23" v-model="h1"></el-input>
                    <a class="font-show">:</a>
                    <el-input type="number" size="small" style="margin:5px; width:60px"  min="0" :max="day1==day2&&h1+1==h2||day1+1==day2&&h1==23&&h2==0?m2:59" v-model="m1"></el-input>
                    <a class="font-show">to</a>
                    <el-input type='number' size="small" style="margin:5px; width:60px"  :min='h1==23&&h2==0||h1+1>h2?day1+1:day1' max='30'  v-model="day2"></el-input>
                    <a class="font-show">-</a>
                    <el-input type="number" size="small" style="margin:5px; width:60px"  :min="day1==day2?h1+1:0" max="23" v-model="h2"></el-input>
                    <a class="font-show">:</a>
                    <el-input type="number" size="small" style="margin:5px; width:60px"  :min="day1==day2&&h1+1==h2||day1+1==day2&&h1==23&&h2==0?m1:0" max="59" v-model="m2"></el-input>
                 </div>
                  <div style="display:flex; width:100%">
                  <div class="block-bg" style="width:49%; margin-right:2%">
                     <span style="height:30px width:50%"class="font-show allCenter">预测范围</span>
                    <el-slider style="margin-left:10px"
                      v-model="aim"
                      :min=10
                      :max=200
                      show-input>
                    </el-slider>
                  </div>

                  <div class="block-bg" style="width:49%">
                     <span style="height:30px width:50%"class="font-show allCenter">Epoch</span>
                    <el-slider style="margin-left:10px"
                      v-model="epoch"
                      :min=50
                      :max=200
                      :step=10
                      show-input>
                    </el-slider>
                  </div>
                  </div>

              <el-button class="button" v-on:click="drawChart"><i style="margin-right:20px"class="el-icon-data-line"></i>Update Chart</el-button>
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

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import { constants } from 'crypto';
import { loadavg } from 'os';
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
//import "https://cdn.bootcss.com/heatmap.js/2.0.2/heatmap.min.js"
//import "https://cdn.jsdelivr.net/npm/leaflet-heatmap@1.0.0/leaflet-heatmap.min.js"
//import "./dmap-dist.js"
//var map = new dmap.Map('container')

export default {
  components:{
    Header,
    VeLine
  },
  data () {
    var aim=50
    var name=""
      var id=""
      var length=""
      var pinyin=""
      var v_data = [0]
      var map_list =[]
      var day1=1,day2=1,h1=0,m1=0,h2=1,m2=4
      //var that = this
    return {
      chartExtend: {
      legend:{
            textStyle: {
            color: '#fff',
          }
      },
      yAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#fff',
            width: 1
          }
        }
      },
      xAxis: {
        axisLine: {
          show: true,
          lineStyle: {
            color: '#fff',
            width: 1
          }          
        }
      }
      },
      chartData: {
          columns: ['Time', 'real_velocity', 'linear_regression','lstm'],
          rows: []
        },
      epoch:100,
      aim:aim,
      day1:day1,
      day2:day2,
      h1:h1,
      h2:h2,
      m1:m1,
      m2:m2,
      current_road:-1,
      current_kind:0,
      v_data:v_data,
      weight:4,
      //weight_clicked:10,
      name:name,
      id:id,
      length:length,
      pinyin:pinyin,
      patterns:[],
      latlngs:[],
      zoom: 12,
      //poly_data_clicked:[],
      center: L.latLng(39.913220,116.419482),
      url: "https://api.mapbox.com/styles/v1/stddeepdark/cjy9ocr5u0azu1cplucbsn6hi/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoic3RkZGVlcGRhcmsiLCJhIjoiY2p5OW8zMDI4MDY3bDNtbzRhMG1xeDc0byJ9._NAqdyJueJNsv2D2rSimwQ",
    //'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
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

        const loading = this.$loading({
          lock: true,
          text: '模型训练中',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });

        this.chartData.rows=[]
        var rows=[]
        var x = [],y = [];
        var i
        var data =[]
        for(i = (this.day1-1)*24*60 + this.h1*60 + this.m1; i < (this.day2-1)*24*60 + this.h2*60 + this.m2; i++)
        {
            data.push(this.v_data[i])
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
        row['lstm']=this.v_data[i]
        rows.push(row)
        
        data.push(this.v_data[i])
        
        i++;
        var lstm_data

        this.$http.get('http://115.28.163.137:8000/get_lstm/?mapid='+this.id+"&data="+data+"&num="+this.aim+"&epoch="+this.epoch)
        .then(function(response){
            if(response.data.error_num != 0)
                alert(response.data.msg)
            else
                lstm_data = response.data.msg
            console.log(response.data.msg)

          for(var u = 0; u < this.aim; u++){
            let row={}
            row['Time']=this.num2time(i+u)
            row['real_velocity']=this.v_data[i+u]
            row['lstm']=lstm_data[u]
            row['linear_regression']=regressionModel.predict(parseFloat(i+u))
            rows.push(row)
          }
          this.chartData.rows=rows
          loading.close();
        })
        .catch((error)=>{
            loading.close();
            alert(error)
        })

          
    },
    load_data:function(){
     // http://25871m8b19.zicp.vip:16559/
     const loading = this.$loading({
          lock: true,
          text: '数据加载中',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });
      this.$http.get('http://115.28.163.137:8000/load_data/?file='+this.id)
        .then(function(response){
            if(response.data.error_num != 0)
                alert(response.data.msg)
            else
                this.v_data = response.data.msg
            loading.close();
        })
        .catch((error)=>{
            alert(error)
            loading.close();
        })
    },
    lineClick:function($event,Pindex,polyline){
                console.log(polyline)
                let index = polyline.index
                this.name=roads["features"][index]["properties"]["Name"];
                var id = roads["features"][index]["properties"]["ID"]
                this.id=roads["features"][index]["properties"]["MapID"] + "_" + roads["features"][index]["properties"]["Kind"]+"0".repeat(4-id.length) + id;
                this.length=roads["features"][index]["properties"]["Length"];
                this.pinyin=roads["features"][index]["properties"]["PinYin"];
                //this.poly_data_clicked=polyline;
                if(this.current_road != -1)
                  this.poly_data[this.current_road]["color"]=this.color
                this.current_road = Pindex  
                console.log('befor')
                this.poly_data[Pindex]["color"]=this.color_clicked
                console.log('after')
                this.load_data();  
                //console.log(this.poly_data_clicked)
    },
    startDraw:function(){
      this.poly_data=[]
        for(var i = 0; i < this.map_list.length; i++) {
          let poly_data = [];
          let index = this.map_list[i]
          for(var u = 0; u < roads["features"][index]["geometry"]["coordinates"].length; u++){
            poly_data.push([roads["features"][index]["geometry"]["coordinates"][u][1],roads["features"][index]["geometry"]["coordinates"][u][0]])
         }
          this.poly_data.push({"line":poly_data,'index':index,"color":this.color})
        }
        //this.poly_data_clicked=[]
    },
    drawRoad: function() {
          if(this.current_kind >= 4)
            this.current_kind = 1
          else
            this.current_kind++
          /*
          var m =[]
          for(var i = 0; i < roads["features"].length; i++) {
            if(roads["features"][i]["properties"]["Kind"] == this.current_kind)
              m.push(i);
          }*/
          this.$http.get('http://115.28.163.137:8000/get_map/?kind='+this.current_kind)
            .then(function(response){
                if(response.data.error_num != 0)
                    alert(response.data.msg)
                else
                {
                  this.map_list = response.data.msg
                  this.startDraw()
                }
                console.log(response.data.msg)
            })
            .catch((error)=>{
                alert(error)
            })
        
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
      
      height:100%;
      height:100%;
  }
  .vue-leaflet{
      width:100%;
      height 80%;
      box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
  .left{
      position:absolute;
      z-index 200;
      width: 50%;
      height: 100%;
      text-align:center;
  }
  .right{
  width 600px
  height 100%
  position absolute
  top 50px
  right 0
  z-index 20
  }
  .chart{
      margin-top 15px;
      background: linear-gradient(to right, rgba(62,73,103,0.7), rgba(48,58,88,1));
      box-shadow 8px 8px 8px rgba(0, 0,0, 0.5);
      margin-bottom 5px;
      width: 100%;
      height: 500px;
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
  .block-bg{
    border-radius:6px; 
    color: #c0c4cc; 
    margin:5px 0; 
    background: linear-gradient(to right, rgba(62,73,103,0.7), rgba(48,58,88,1));
    box-shadow 8px 8px 8px rgba(0, 0,0, 0.5);   
  }
  .font-bg{
    color: #c0c4cc
    font-family:"微软雅黑";
    font-size: 1em;
  }
  .font-show{
    color #13ffd7
    font-family:"微软雅黑";
    font-size: 1em;
  }
  .allCenter{
    display:flex;
    justify-content:center;
    align-items:center;
  }
  .menu
    position absolute
    left 40px
    bottom 20px
  .button
        background: #303a58;
        border: 1px solid #303a58;
        color: #c0c4cc; 

  .button:hover
        background: #303a58;
        color #13ffd7
</style>
