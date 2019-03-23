<template>

  <v-toolbar fixed dark color="#322c28" app>
    <span class="group pa-0">
      <v-btn flat icon  :to="{ path: '/' }">
        <v-icon large dark>home</v-icon>
        </v-btn>
      </span>
    <v-toolbar-title>自动化试卷生成及批改系统</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
  <v-btn flat v-for="item in items" :to="{ path: item[1] }">{{item[0]}}</v-btn>     
    </v-toolbar-items>
  </v-toolbar>
</template>
<script>
     export default {
        data: () => ({
            items: [
              ["题库管理","/Tiku"],["座位生成","/zhuowei"],
              ["改卷系统","/chouti"]
              ]
        }),
        mounted() {
        }
    }
</script>

<style>
    /*@import url('https://fonts.loli.net/css?family=Roboto:300,400,500,700|Material+Icons');*/
    /* 由于网站加载的比较慢，所以直接使用link标签，放到了index.ejs里了 */
    /* Global CSS */
</style>


