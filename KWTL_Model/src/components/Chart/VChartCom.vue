<template>
  <div id="vchart-com">
    <div v-for="(chart,index) in curChartList" :key="index" :class="curChartList.length - 1 == index ? 'lastHeight':''">
      <div v-for="(item,index) in chart" :key="index">
        <p class="chart-legend"><span>{{item.title}}</span><cite :class="curLegendActive == index ? 'legendActive':''"></cite></p>
        <div class="column">
          <!-- 分组柱图 -->
          <!-- :settings="curSettingStack" -->
          <ve-histogram v-if="item.type=='histogram'" width="100%" height="100%" :judge-width="true" :colors="curColor" :data-zoom="curDataZoom" :data="item.data" :extend="curExtend"></ve-histogram>
          <!-- 堆叠柱图 -->
          <ve-histogram v-if="item.type=='histogramStack'" width="100%" height="100%" :judge-width="true" :colors="curColor" :data="item.data" :extend="curExtend" :settings="chartSettings"></ve-histogram>
          <!-- 折线柱图 -->
          <ve-histogram v-if="item.type=='histogramLine'" width="100%" height="100%" :judge-width="true" :colors="curColor" :data="item.data" :extend="curExtend" :settings="chartSettings"></ve-histogram>
          <!-- 折线图 -->
          <ve-line v-if="item.type=='line'" width="100%" height="100%" :judge-width="true" :colors="curColor" :data="item.data" :extend="curExtend"></ve-line>
          <!-- 饼图 -->
          <ve-pie v-if="item.type == 'pie'" width="100%" height="100%" :judge-width="true" :colors="curColor" :data="item.data"  :extend="curExtend" :settings="curSettingPie"></ve-pie>
          <!-- <ve-ring v-if="item.type=='ring'" :height="curHeight" :colors="curColor" :data="item.data"  :extend="curExtend" :settings="curSettingRing"></ve-ring> -->
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import _ from 'lodash'

// *图表组件配置项扩展方法：https://www.jianshu.com/p/46d844355f50

export default {
  name:'vchart-com',
  data(){
    return {
      // 数据结构
      curChartList: [
          [{
              title: 'XXXX图表1',
              type: 'histogram',
              data: {
                  columns: ['日期', '访问用户', '下单用户', '下单率'],
                  rows: [
                      { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                      { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
                      { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
                      { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
                      { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
                      { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
                  ]
              }
          }],
          [{
                  title: 'XXXX图表2',
                  type: 'line',
                  data: {
                      columns: ['日期', '访问用户', '下单用户', '下单率'],
                      rows: [
                          { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                          { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
                          { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
                          { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
                          { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
                          { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
                      ]
                  }
              },
              {
                  title: '',
                  type: 'histogram',
                  data: {
                      columns: ['日期', '访问用户', '下单用户', '下单率'],
                      rows: [
                          { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                          { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
                          { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
                          { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
                          { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
                          { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
                      ]
                  }
              }
          ],
          [{
              title: 'XXXX图表1',
              type: 'histogram',
              data: {
                  columns: ['日期', '访问用户', '下单用户', '下单率'],
                  rows: [
                      { '日期': '1/1', '访问用户': 1393, '下单用户': 1093, '下单率': 0.32 },
                      { '日期': '1/2', '访问用户': 3530, '下单用户': 3230, '下单率': 0.26 },
                      { '日期': '1/3', '访问用户': 2923, '下单用户': 2623, '下单率': 0.76 },
                      { '日期': '1/4', '访问用户': 1723, '下单用户': 1423, '下单率': 0.49 },
                      { '日期': '1/5', '访问用户': 3792, '下单用户': 3492, '下单率': 0.323 },
                      { '日期': '1/6', '访问用户': 4593, '下单用户': 4293, '下单率': 0.78 }
                  ]
              }
          }
          ]
      ]
    }
  },
}
</script>

<style lang="stylus" scoped>
#vchart-com
  width 100%
  height calc(100% - 120px)
  // ~~~~~~~~~~~~~竖向均匀分布
  display flex
  flex-direction column
  justify-content center
  // ~~~~~~~~~

#vchart-com > div
  // ~~~~~~~~~竖向撑满
  flex 1 
  // ~~~~~~~~~
  width 100%
  box-sizing border-box 
  background: linear-gradient(to right,rgba(62,73,103,0.7) , rgba(48,58,88,1))
  -webkit-box-shadow 8px 8px 8px rgba(0,0,0,0.5)
  box-shadow 8px 8px 8px rgba(0,0,0,0.5)
  margin-bottom 10px
  // ~~~~~~横向
  display flex
  flex-direction row
  align-items center

#vchart-com > div > div
// ~~~~~~横向
  flex 1
  height 100%

#vchart-com
  .lastHeight
    margin-bottom 25px

.chart-legend
  position relative
  // 解决多个图表标题问题
  height 30px
  line-height 30px
  margin-left 10px

.chart-legend span
  display inline-block
  font-size 16px
  color #fff

.chart-legend cite.legendActive
  position absolute
  left 0
  top 0
  width 5px
  height 30px
  background #13ffd7
  margin-left -10px

#vchart-com > div > div .column
  height calc(100% - 30px)

</style>
