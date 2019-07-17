// 索引页
<template>
<div>
    <Header/>

    <div class="links">
        <div>
            <router-link to="/timeSeries">通州</router-link>
        </div>
        <div>
            <router-link to="/timeSeries2">亦庄</router-link>
        </div>
        <div>
            <router-link to="/page1">数据</router-link>
        </div>
        <div>
            <router-link to="/page2">模型</router-link>
        </div>
    </div>
</div>
</template>

<script>
import Header from '@/components/Header/index.vue'

export default {
    components:{
        Header
    }
}
</script>

<style lang="stylus" scoped>
.links
    display flex
    height 100%

    &>div
        flex 1
        height 100%

        
        a
            display block
            margin 0 auto
            width 70%
            height 70%
            margin-top 15%
            text-align center
            font-size 33px
            line-height 100px
            transition .3s
            color rgba(255,255,255,.7)
            opacity .7
            background #34495e

            &:hover
                width 80%
                height 80%
                margin-top 10%
                color #fff
                opacity 1



</style>
