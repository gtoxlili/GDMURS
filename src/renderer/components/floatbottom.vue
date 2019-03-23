<template>
  <v-card id="create">
    <v-speed-dial
      v-model="fab"
      :top="top"
      :bottom="bottom"
      :right="right"
      :left="left"
      :direction="direction"
      :open-on-hover="hover"
      :transition="transition"
    >
      <template v-slot:activator>
        <v-btn 
          v-model="fab"
          color="#00695b"
          dark
          fab
        >
          <v-icon>list</v-icon>
          <v-icon>close</v-icon>
        </v-btn>
      </template>
      <v-btn
        @click="childClick('attach_file')"
        fab
        dark
        small
        color="#726250"
      >
        <v-icon>attach_file</v-icon>
      </v-btn>
      <v-btn
        @click="childClick('add')"
        fab
        dark
        small
        color="#6b818e"
      >
        <v-icon>add</v-icon>
      </v-btn>
      <v-btn
        @click="childClick('cloud_upload')"
        fab
        dark
        small
        color="#003149"
      >
        <v-icon>cloud_upload</v-icon>
      </v-btn>
      <v-btn
        @click="childClick('red')"
        fab
        dark
        small
        color="#a04940"
      >
        <v-icon>cloud_download</v-icon>
      </v-btn>
    </v-speed-dial>
  </v-card>
</template>

<style>
  /* This is for documentation purposes and will not be needed in your application */
  #create .v-speed-dial {
    position: fixed;
  }

  #create .v-btn--floating {
    position: relative;
  }
</style>

<script>
  export default {
    data: () => ({
      direction: 'top',
      fab: false,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: true,
      bottom: true,
      left: false,
      transition: 'slide-y-reverse-transition'
    }),methods: {
      childClick (xsw) {
        // childByValue是在父组件on监听的方法
        // 第二个参数this.childValue是需要传的值
        this.$emit('childByValue', xsw)
      }
    },
    computed: {
      activeFab () {
        switch (this.tabs) {
          case 'one': return { 'class': 'purple', icon: 'account_circle' }
          case 'two': return { 'class': 'red', icon: 'edit' }
          case 'three': return { 'class': 'green', icon: 'keyboard_arrow_up' }
          default: return {}
        }
      }
    },
  }
</script>