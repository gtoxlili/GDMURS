<template>
 <div id="app">
   <Navbar></Navbar> 
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
export default {
  name: 'app',
  components: {
    Navbar
  }
};
</script>

<style>
/*@import url('https://fonts.loli.net/css?family=Roboto:100,300,400,500,700,900|Material+Icons');*/
  /* CSS */
@font-face {
  font-family: Snickles;
  src: url('hwxh.ttf');
}
div{
  font-family:"Snickles";
}
</style>