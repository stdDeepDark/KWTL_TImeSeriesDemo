// 索引页
<template>
<div>
    <Header/>

    <div class="links">
        <div>
            <router-link to="">个体行为预测Demo</router-link>
        </div>
    
        <div>
            <router-link to="/hazardousArticle">危险品Demo</router-link>
        </div>
        <div>
            <router-link to="/cityGroup">城市组团Demo</router-link>
        </div>
        <div>
            <router-link to="/timeSeries">时间序列Demo</router-link>
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
