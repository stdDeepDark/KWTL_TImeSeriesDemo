<template>
    <div>
      <!-- 头部 -->
      <Header/>
      <!-- 主体 -->
      <div class="main">
          <!-- 添加代码 -->
            <div id="lefe" class="container">
              <div class="amap-wrapper">
                <el-amap class="amap-box" :amap-manager="amapManager" :zoom="zoom" :mapStyle="mapStyle" :vid="'amap-vue'">
                    <el-amap-polyline :events="lineEvents" v-for="(polyline,index) in poly_data" :path="polyline.path" :extData="index" :strokeColor="strokeColor"></el-amap-polyline>
                    <el-amap-polyline :zIndex="zIndex_clicked" :path="poly_data_clicked" :strokeWeight="strokeWeight_clicked" :strokeColor="strokeColor_clicked"></el-amap-polyline>
                </el-amap>
              </div>
               <button v-on:click="drawRoad"> Show Road Network</button>  
            </div>
            <a>{{name}}-{{id}}-{{pinyin}}-{{length}}</a>    
            
            <a>{{mapid}}</a>           
        </div>
      </div>
</template>


<!-- 先引入 Vue -->
<script src="https://unpkg.com/vue/dist/vue.js"></script>
<!-- 引入组件库 -->
<script src="https://unpkg.com/vue-amap/dist/index.js"></script>

<script>
import Header from '@/components/Header/index.vue'
import VueAMap from 'vue-amap'
import { AMapManager } from 'vue-amap';
//import { lazyAMapApiLoaderInstance } from 'vue-amap';

import roads from './1.json'
console.log(roads)
import Vue from 'vue';
import vueResource from 'vue-resource'
Vue.use(vueResource)
Vue.use(VueAMap);

VueAMap.initAMapApiLoader({
  key: '194707d60368d573749c6079e36f8e69',
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor'],
  // 默认高德 sdk 版本为 1.4.4
  uiVersion: '1.0', // ui库版本，不配置不加载,
  v: '1.4.4',
});
/*
lazyAMapApiLoaderInstance.load().then(() => {
  // your code ...
  this.map = new AMap.Map('left', {
    center: new AMap.LngLat(11.59996, 31.197646)
  });
});
*/
let amapManager = new VueAMap.AMapManager();

export default {
    components:{
        Header
    },
    data(){
      var name="name"
      var id="id"
      var length="length"
      var pinyin="pinyin"
      var poly_data_clicked=[]
      var that = this
      var curr_map = 0
        return {
          mapid:[],
          zIndex_clicked:100,
          strokeWeight_clicked:10,
            name:name,
            id:id,
            amapManager,
            length:length,
            pinyin:pinyin,
            zoom:[8,15],
            poly_data:[],
            id:id,
            poly_data_clicked:poly_data_clicked,
            strokeColor:"#BEE7E9",
            strokeColor_clicked:"#F4606C",
            mapStyle:"amap://styles/8b2dea8e6eacedfe170970e925ba09a1", //设置地图样式
            lineEvents: {
              click(e) {
                alert('click polyline');
                var index= e.target.getExtData();
                that.name=roads["features"][index]["properties"]["Name"];
                var id = roads["features"][index]["properties"]["ID"]
                that.id=roads["features"][index]["properties"]["MapID"] + "_" + roads["features"][index]["properties"]["Kind"]+"0".repeat(4-id.length) + id;
                that.length=roads["features"][index]["properties"]["Length"];
                that.pinyin=roads["features"][index]["properties"]["PinYin"];
                that.poly_data_clicked=e.target.getPath();
                console.log(that.poly_data_clicked)
              },
              end: (e) => {
               
              }
            }
        }
    },
    mounted(){
      //let mapid = new Set()
        /*for(var i = 0; i < roads["features"].length; i++) {
            mapid.add(roads["features"][i]["properties"]["MapID"])
        }
        this.mapid=[...mapid]*/
      //this.drawRoad()
      //this.add()
    },
    methods: {
      drawRoad: function() {
        
        console.log(this.mapid[this.curr_map])  
        let poly_data = [];
        for(var i = 0; i < 1000; i++) {
            poly_data.push({path : roads["features"][i]["geometry"]["coordinates"]})
        }
        this.poly_data = poly_data;
        
      console.log(roads["features"].length);
        console.log(mapid);
      
      },
      add() {
        let o = amapManager.getMap();

        for(var i = 0; i < 2000; i++) {
            let path = [];
            path=roads["features"][i]["geometry"]["coordinates"]
            

            // 创建折线实例
            var polyline = new AMap.Polyline({
                path: path,  
                borderWeight: 2, // 线条宽度，默认为 1
                strokeColor: 'red', // 线条颜色
                lineJoin: 'round' // 折线拐点连接处样式
            });

            // 将折线添加至地图实例
            o.add(polyline);
        }

      }
    }

}
</script>

<style lang="stylus" scoped>
.main
    height 100%
.amap-wrapper {
  width: 800px;
  height: 400px;
  margin:50px 50px;
}
.container {
  width: 900px;
}
</style>


