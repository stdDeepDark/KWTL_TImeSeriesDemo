// 方式2：iframe调用外链
<template>
    <div>
        <!-- 头部 -->
        <Header/>
        <!-- 主体 -->
        <div class="main">
            <iframe class="my-iframe" 
                src="http://www.baidu.com" 
                frameborder="0" 
                scrolling="no"
                height="100%"
                width="100%"></iframe>
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
.main
    height 100%
</style>
