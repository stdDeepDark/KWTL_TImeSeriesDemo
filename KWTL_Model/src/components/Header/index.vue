<template>
  <div class="header-wrap">

    <div class="header-bar">
      <div class="title">
        <h1>基于社会行为数据城市认知系统</h1>
      </div>
      <router-link class="back-home" to="/">返回首页</router-link>
    </div>

  </div>
</template>

<script>
export default {

};
</script>

<style lang="stylus" scoped>
.header-wrap
  position relative
  width 100%
  height 50px
  background #00203e

  .header-bar
    height 100%
    position relative
    border-top 2px solid #00f6ff

    .title
      height 60px
      width 580px
      background url('../../assets/bg/logo_bg.png') no-repeat
      background-size 100% 100%
      position absolute
      z-index 1
      left 50%
      top -2px
      margin-left -302.5px

      h1
        letter-spacing 2px
        line-height 64px
        font-size 24px
        color #fff
        margin 0 auto
        text-align center    

    .back-home
      color #fff
      line-height 40px
      margin-right 30px


.back-home
  float:right
</style>