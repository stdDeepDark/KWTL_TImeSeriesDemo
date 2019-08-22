// 方式1：代码嵌入
<template>
    <div>
        <!-- 头部 -->
        <Header/>
        <!-- 主体 -->
        <div class="main">
            <!-- 添加代码 -->
            <div class="amap-wrapper">
                <el-amap class="amap-box" :zoom="zoom" :mapStyle="mapStyle" :vid="'amap-vue'">
                    <el-amap-polyline  v-for="polyline in poly_data" :path="polyline.path"></el-amap-polyline>
                </el-amap>
            </div>
            <button v-on:click="drawRoad"> Show Road Network</button>  
        </div>
    </div>
</template>
<script>
import VueAMap from 'vue-amap'
import roads from './1.json'
console.log(roads)
import Vue from 'vue';
import vueResource from 'vue-resource'
Vue.use(vueResource)
import Header from '@/components/Header/index.vue'


Vue.use(VueAMap);

VueAMap.initAMapApiLoader({
  key: 'abcf441d8ae25a58d7f6b0781bcb7347',
  plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor'],
  // 默认高德 sdk 版本为 1.4.4
  v: '1.4.4'
});

export default {
    components:{
        Header
    },
    data(){
        return {
            zoom:10,
            poly_data:[],
            mapStyle:"amap://styles/8b2dea8e6eacedfe170970e925ba09a1", //设置地图样式
        }
    },
    methods: {
      drawRoad: function() {
        let poly_data = [];
        for(var i = 0; i < roads["features"].length; i++) {
            poly_data.push({path : roads["features"][i]["geometry"]["coordinates"]})
        }
        console.log(poly_data)
        this.poly_data = poly_data;
      }
    }

}
</script>

<style lang="stylus" scoped>
.main
    height 100%

.amap-wrapper {
  width: 800px;
  height: 550px;
}
</style>
