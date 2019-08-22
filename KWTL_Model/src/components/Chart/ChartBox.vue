<template>
  <div class="chart-wrap">
    <!-- 指标信息 -->
    <figure-com/>
    <!-- V-chart 图表 -->
    <vchart-com/>
    <!-- 之前封装的antV-->
    <!-- <chart-com :chartList="curChartData"></chart-com> -->
    
  </div>
</template>

<script>
import FigureCom from '@/components/Chart/FigureCom'
import VchartCom from '@/components/Chart/VChartCom'
// import ChartCom from './common/ChartCom.vue'

export default {
  name: 'chart-wrap',
  components:{
    FigureCom,
    VchartCom
    // ChartCom
  },
  // computed:{
  //   curChartData(){
  //     return this.$store.getters['chart/curChartData']
  //   }
  // },
  // created(){
  //   //触发
  //   this.$store.dispatch('chart/updatechart',0)
  // }
}
</script>

<style lang="stylus">
.chart-wrap
  width 31%
  height 100%
  position absolute
  top 35px
  right 0
  z-index 20
  min-width 540px
</style>
