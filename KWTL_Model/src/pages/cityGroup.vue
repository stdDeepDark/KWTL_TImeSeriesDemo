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
                <!--
                <ChartBox/>
                -->
            </div>
            <!-- 菜单 -->
            <div class="menu">
                <el-button v-on:click="settaz"> 显示小区</el-button>
                <el-button v-on:click="ereasetaz"> 清除小区</el-button> 
                <el-button v-on:click="drawzones"> 显示大区</el-button>
                <el-button v-on:click="ereasezone"> 清除大区</el-button>
            </div>
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header/index.vue'
import ChartBox from '@/components/Chart/ChartBox.vue'
import zones from './zone_new.json'
import tazdata from './taz_new.json'

export default {
    components:{
        Header,
        ChartBox
    },
    data(){
        return{
            zone: [[116.254,39.961],[116.309,39.992],[116.389,40.002],[116.468,39.986],
                   [116.349,39.954],[116.408,39.972],[116.242,39.902],[116.324,39.921],
                   [116.41,39.933],[116.451,39.926],[116.498,39.933],[116.317,39.88],
                   [116.386,39.888],[116.494,39.869],[116.276,39.832],[116.355,39.815],
                   [116.426,39.824]],
            map: null,
            gridLayer: null,

            pg1: null,
            pg2: null,
            pg3: null,
            pg4: null,
            pg5: null,
            pg6: null,
            pg7: null,
            pg8: null,
            pg9: null,
            pg10: null,
            pg11: null,
            pg12: null,
            pg13: null,
            pg14: null,
            pg15: null,
            pg16: null,
            pg17: null,

            line1: null,
            line2: null,
            line3: null,
            line4: null,
            line5: null,
            line6: null,
            line7: null,
            line8: null,
            line9: null,
            line10: null,
            line11: null,
            line12: null,
            line13: null,
            line14: null,
            line15: null,
            line16: null,
            line17: null,
            number: 7,
            line: null,
            time: 0,
            taz: null,
            tazs: null,
            tazgroup: null,
            count: 0,
            str: 0,
            tazdata: null,
        }
    },
    mounted(){
        this.map = new AMap.Map('container', {
            mapStyle: 'amap://styles/dark',
            center:[116.5, 39.9],
            zoom:11
        });
        this.pg1 = new AMap.Polygon({
            path: zones["geometries"][3]["coordinates"],  
            fillColor: '#DC143C', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度 
        });
        this.pg2 = new AMap.Polygon({
            path: zones["geometries"][0]["coordinates"],  
            fillColor: '#4B0082', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
            
        });
        this.pg3 = new AMap.Polygon({
            path: zones["geometries"][1]["coordinates"],  
            fillColor: '#EE82EE', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg4 = new AMap.Polygon({
            path: zones["geometries"][6]["coordinates"],  
            fillColor: '#4169E1', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg5 = new AMap.Polygon({
            path: zones["geometries"][7]["coordinates"],  
            fillColor: '#00FFFF', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg6 = new AMap.Polygon({
            path: zones["geometries"][8]["coordinates"],  
            fillColor: '#3CB371', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg7 = new AMap.Polygon({
            path: zones["geometries"][5]["coordinates"],  
            fillColor: '#FFFFF0', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg8 = new AMap.Polygon({
            path: zones["geometries"][10]["coordinates"],  
            fillColor: '#FFFF00', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg9 = new AMap.Polygon({
            path: zones["geometries"][9]["coordinates"],  
            fillColor: '#FFA500', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg10 = new AMap.Polygon({
            path: zones["geometries"][12]["coordinates"],  
            fillColor: '#FF0000', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg11 = new AMap.Polygon({
            path: zones["geometries"][4]["coordinates"],  
            fillColor: '#808080', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg12 = new AMap.Polygon({
            path: zones["geometries"][13]["coordinates"],  
            fillColor: '#000000', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg13 = new AMap.Polygon({
            path: zones["geometries"][11]["coordinates"],  
            fillColor: '#556B2F', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg14 = new AMap.Polygon({
            path: zones["geometries"][15]["coordinates"],  
            fillColor: '#000080', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg15 = new AMap.Polygon({
            path: zones["geometries"][2]["coordinates"],  
            fillColor: '#FFC0CB', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg16 = new AMap.Polygon({
            path: zones["geometries"][14]["coordinates"],  
            fillColor: '#AFEEEE', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg17 = new AMap.Polygon({
            path: zones["geometries"][16]["coordinates"],  
            fillColor: '#90EE90', // 多边形填充颜色
            borderWeight: 1, // 线条宽度，默认为 1
            strokeColor: 'red', // 线条颜色
            fillOpacity: "0.5" //覆盖透明度
        });
        this.pg1.on('click',this.click1);
        this.pg2.on('click',this.click2);
        this.pg3.on('click',this.click3);
        this.pg4.on('click',this.click4);
        this.pg5.on('click',this.click5);
        this.pg6.on('click',this.click6);
        this.pg7.on('click',this.click7);
        this.pg8.on('click',this.click8);
        this.pg9.on('click',this.click9);
        this.pg10.on('click',this.click10);
        this.pg11.on('click',this.click11);
        this.pg12.on('click',this.click12);
        this.pg13.on('click',this.click13);
        this.pg14.on('click',this.click14);
        this.pg15.on('click',this.click15);
        this.pg16.on('click',this.click16);
        this.pg17.on('click',this.click17);
        //x+0.0055 y+0.0015
        /*
        for(var i = 0; i < tazdata["features"].length; i++){
            for(var j = 0; j < tazdata["features"][i]["coordinates"].length; j++){
                this.str = tazdata["features"][i]["coordinates"][j].toString()
                var strs = this.str.split(",");
                tazdata["features"][i]["coordinates"][j] = [parseFloat(strs[0]),parseFloat(strs[1])]
            }
        }
        for(var i = 0; i < zones["geometries"].length; i++){
            for(var j = 0; j < zones["geometries"][i]["coordinates"][0].length; j++){
                this.str = zones["geometries"][i]["coordinates"][0][j].toString()
                var strs = this.str.split(",");
                tazdata["features"][i]["coordinates"][0][j] = [parseFloat(strs[0]),parseFloat(strs[1])]
            }
        }*/
        this.tazs = [];
        for(var i = 0; i < tazdata["features"].length; i++){
            this.taz = new AMap.Polygon({
                path: tazdata["features"][i]["coordinates"],
                fillOpacity: "0.1"
            });
            this.tazs.push(this.taz);
        }
        this.tazgroup = new AMap.OverlayGroup(this.tazs);
        
        //alert("地图加载完毕");
    },
    methods:{
        settaz: function(){
            this.map.add(this.tazgroup);
        },
        ereasetaz: function(){
            this.map.remove(this.tazgroup);
        },
        setlines: function(){
            if(this.time != 0){
                this.ereaselines();
            }
            this.time = this.time+1;
            this.line1 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[0]],
                showDir: "true",
            });
            this.line2 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[1]],
                showDir: "true",
            });
            this.line3 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[2]],
                showDir: "true"
            });
            this.line4 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[3]],
                showDir: "true"
            });
            this.line5 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[4]],
                showDir: "true"
            });
            this.line6 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[5]],
                showDir: "true"
            });
            this.line7 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[6]],
                showDir: "true"
            });
            this.line8 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[7]],
                showDir: "true"
            });
            this.line9 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[8]],
                showDir: "true"
            });
            this.line10 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[9]],
                showDir: "true"
            });
            this.line11 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[10]],
                showDir: "true"
            });
            this.line12 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[11]],
                showDir: "true"
            });
            this.line13 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[12]],
                showDir: "true"
            });
            this.line14 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[13]],
                showDir: "true"
            });
            this.line15 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[14]],
                showDir: "true"
            });
            this.line16 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[15]],
                showDir: "true"
            });
            this.line17 = new AMap.BezierCurve({
                path: [this.zone[this.number-1],this.zone[16]],
                showDir: "true"
            });
        },
        drawlines: function(){
            this.map.add(this.line1);
            this.map.add(this.line2);
            this.map.add(this.line3);
            this.map.add(this.line4);
            this.map.add(this.line5);
            this.map.add(this.line6);
            this.map.add(this.line7);
            this.map.add(this.line8);
            this.map.add(this.line9);
            this.map.add(this.line10);
            this.map.add(this.line11);
            this.map.add(this.line12);
            this.map.add(this.line13);
            this.map.add(this.line14);
            this.map.add(this.line15);
            this.map.add(this.line16);
            this.map.add(this.line17);
        },
        ereaselines: function(){
            this.map.remove(this.line1);
            this.map.remove(this.line2);
            this.map.remove(this.line3);
            this.map.remove(this.line4);
            this.map.remove(this.line5);
            this.map.remove(this.line6);
            this.map.remove(this.line7);
            this.map.remove(this.line8);
            this.map.remove(this.line9);
            this.map.remove(this.line10);
            this.map.remove(this.line11);
            this.map.remove(this.line12);
            this.map.remove(this.line13);
            this.map.remove(this.line14);
            this.map.remove(this.line15);
            this.map.remove(this.line16);
            this.map.remove(this.line17);
        },
        click1: function( ){
            this.number = 1;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click2: function( ){
            this.number = 2;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click3: function( ){
            this.number = 3;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click4: function( ){
            this.number = 4;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click5: function( ){
            this.number = 5;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click6: function( ){
            this.number = 6;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click7: function( ){
            this.number = 7;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click8: function( ){
            this.number = 8;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click9: function( ){
            this.number = 9;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click10: function( ){
            this.number = 10;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click11: function( ){
            this.number = 11;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click12: function( ){
            this.number = 12;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click13: function( ){
            this.number = 13;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click14: function( ){
            this.number = 14;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click15: function( ){
            this.number = 15;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click16: function( ){
            this.number = 16;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        click17: function( ){
            this.number = 17;
            this.setlines();
            this.drawlines();
            //alert('click here at zonenumber:' + this.number);
        },
        drawzones: function(){
            this.map.add(this.pg1);
            this.map.add(this.pg2);
            this.map.add(this.pg3);
            this.map.add(this.pg4);
            this.map.add(this.pg5);
            this.map.add(this.pg6);
            this.map.add(this.pg7);
            this.map.add(this.pg8);
            this.map.add(this.pg9);
            this.map.add(this.pg10);
            this.map.add(this.pg11);
            this.map.add(this.pg12);
            this.map.add(this.pg13);
            this.map.add(this.pg14);
            this.map.add(this.pg15);
            this.map.add(this.pg16);
            this.map.add(this.pg17);
        },
        ereasezone: function(){
            this.map.remove(this.pg1);
            this.map.remove(this.pg2);
            this.map.remove(this.pg3);
            this.map.remove(this.pg4);
            this.map.remove(this.pg5);
            this.map.remove(this.pg6);
            this.map.remove(this.pg7);
            this.map.remove(this.pg8);
            this.map.remove(this.pg9);
            this.map.remove(this.pg10);
            this.map.remove(this.pg11);
            this.map.remove(this.pg12);
            this.map.remove(this.pg13);
            this.map.remove(this.pg14);
            this.map.remove(this.pg15);
            this.map.remove(this.pg16);
            this.map.remove(this.pg17);
            this.ereaselines();
        }
    },
}
</script>

<style lang="stylus" scoped>
.main
    height 100%
.chart-box
    height 100%
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

</style>
