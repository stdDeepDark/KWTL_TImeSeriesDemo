<template>
  <div class="chart-figure mb" >
    <p class="chart-title"><span>关键指数</span><cite></cite></p>
    <div class="figure-con">
      <div v-for="(item,index) in curFigureList" :key="index" :class="curFigureList.length - 1 == index ? 'line':''">
          <p class="figure-name" :class="item.children ? 'active':''" >{{item.title}}</p>
          <div class="figure-num-wrap">
            <!-- subline -->
              <div class="figure-num" :class="item.children ? '':''"> {{item.value}}<span class="figure-unit">{{item.unit}}</span></div>
              <div class="figure-sub-wrap" v-if="item.children">
                <div v-for="(child,i) in item.children" :key="i">{{ child.title }}<span>{{ child.value }}</span>{{child.unit}}<span>{{child.zb}}</span><br></div>
              </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      curFigureList:[
        {
            title: '流入',
            value: 88123,
            unit: '人',
            children: [{
                    title: 'A 区域流入',
                    value: 14738,
                    unit: '人'
                },
                {
                    title: 'B 区域流入',
                    value: 18237,
                    unit: '人',
                }
            ]
        },
        {
            title: '流出',
            value: 19208,
            unit: '人',
            children:[
              {
                title:'A 区域流入',
                value:14738,
                unit: '人',
              },
              {
                title:'B 区域流入',
                value:18237,
                unit: '人',
              }
            ]
        }
      ]
    }
    
  }
}
</script>

<style lang="stylus" scoped>
/* 子组件公用的样式 */
.chart-figure
  width 100%
  height 105px
  margin-top 15px
  background: linear-gradient(to right, rgba(62,73,103,0.7), rgba(48,58,88,1));
  box-shadow 8px 8px 8px rgba(0, 0,0, 0.5)
  margin-bottom 10px

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
    

.figure-con
  display -webkit-flex
  display flex
  box-sizing border-box
  text-align center

.figure-con > div
  flex 1
  border-right 2px solid #00ffbc

.figure-con > div.line
  border none

.figure-name
  color #fff
  font-size 16px

.figure-name.active
  text-align left
  padding-left 16px

.figure-num-wrap
  display flex

.figure-num-wrap > div
  flex 1
  
.figure-num
  color rgb(0,255,188)
  font-size 30px
  font-weight bold
  
.figure-unit
  font-size 16px
  font-weight normal 

.figure-sub-wrap
  color #8f8f8f
  font-size 11px
  text-align center

.figure-sub-wrap > div
  padding 2px 0
  margin-left -25px

.subline
  border-right 2px solid #989898

</style>

