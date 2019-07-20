<template>
    <div>
        <!-- 头部 -->
        <Header/>
        
        <!-- 主体 -->
        <div id="map-canvas" style="width:500px; height:500px;">
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
//import loadJs from './loadJs'
import jQuery from 'jquery'
//import "https://cdn.bootcss.com/heatmap.js/2.0.2/heatmap.min.js"
//import "https://cdn.jsdelivr.net/npm/leaflet-heatmap@1.0.0/leaflet-heatmap.min.js"
//import "./dmap-dist.js"
//var map = new dmap.Map('container')

export default {
  components:{
    Header,
    VeLine
  },
    
    data() {
          return {}
        },
        methods: {
            draw:function(){
                var testData = {
                max: 8,
                data: [{lat: 24.6408, lng:46.7728, count: 3},{lat: 50.75, lng:-1.55, count: 1}]
                };

                var baseLayer = L.tileLayer(
                'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
                    attribution: '...',
                    maxZoom: 18
                }
                );

                var cfg = {
                // radius should be small ONLY if scaleRadius is true (or small radius is intended)
                // if scaleRadius is false it will be the constant radius used in pixels
                "radius": 2,
                "maxOpacity": .8,
                // scales the radius based on map zoom
                "scaleRadius": true,
                // if set to false the heatmap uses the global maximum for colorization
                // if activated: uses the data maximum within the current map boundaries
                //   (there will always be a red spot with useLocalExtremas true)
                "useLocalExtrema": true,
                // which field name in your data represents the latitude - default "lat"
                latField: 'lat',
                // which field name in your data represents the longitude - default "lng"
                lngField: 'lng',
                // which field name in your data represents the data value - default "value"
                valueField: 'count'
                };


                var heatmapLayer = new HeatmapOverlay(cfg);

                var map = new L.Map('map-canvas', {
                center: new L.LatLng(25.6586, -80.3568),
                zoom: 4,
                layers: [baseLayer, heatmapLayer]
                });

                heatmapLayer.setData(testData);
            }
        },
        beforeMount(){
            let recaptchaScript = document.createElement('script')
            recaptchaScript.async = true
            recaptchaScript.defer = true
            recaptchaScript.setAttribute('src', './heatmap')
            document.head.appendChild(recaptchaScript)
            let recaptchaScript2 = document.createElement('script')
            recaptchaScript2.async = true
            recaptchaScript2.defer = true
            recaptchaScript2.setAttribute('src', './leaflet-heatmap')
            document.head.appendChild(recaptchaScript2)
           
        },
        mounted() {
            this.draw()
        }
      }
</script>


<style lang="stylus" scoped>
  .main{
      position:absolute;
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
</style>
