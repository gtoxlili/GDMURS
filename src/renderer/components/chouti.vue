<template>
  <v-layout row>
     <v-flex xs12 sm3 >
    <template>
  <v-navigation-drawer permanent class="mt-0">
    
    
<v-toolbar flat color="translate">
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>
    <v-divider></v-divider>

    <v-container fluid grid-list-md>
      <v-layout child-flex wrap>
        <v-flex xs12 class="ml-3">
          <v-subheader >Options</v-subheader>
          <v-checkbox v-model="hover" disabled label="阅卷权限" hide-details></v-checkbox>
        </v-flex>
        <v-flex xs12 class="mt-2 ml-3">
          <v-subheader>考试信息</v-subheader>
          <v-text-field
            solo
            v-model="shijuan.keyid"
            label="Message"
            append-icon="search"
            @click:append="xuanzekaos()"
          ></v-text-field>
        </v-flex>
        <v-flex xs12 class="mt-2 ml-3">
          <v-subheader>考生信息</v-subheader>
          <v-text-field
            solo
            label="Message"
            v-model="kaochang.objectId"
            append-icon="search"
            @click:append="xuanzekaoc()"
          ></v-text-field>
        </v-flex></br></br>
       <v-flex xs12 class="mt-2 ml-5">
        <v-btn class="mt-5" color="primary" dark @click="showFileDialog()">选择试卷</v-btn>
        <v-btn class="mt-5" color="primary" :disabled="shijuan==''||kaochang==''" dark @click="kaishijuejuan()">{{ksyjxx}}</v-btn>
          
         </v-flex>
         </br></br></br>
      </v-layout>
    </v-container>


  </v-navigation-drawer>
</template>



</v-flex>
    <v-flex xs12 sm9>
     
        </br>
      <v-card v-if="shifkaishiyj">
        <v-toolbar flat color="translate">
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>
    
    <v-flex xs12 sm10 offset-sm1>
      <v-card-title primary-title>
           <div>
            <h3 class="headline mb-0">{{muqiant[muqian]}}</h3>
            </div>
          </v-card-title>
      <v-card>
        <v-img
          :src="domotu[muqian]"
        ></v-img>
      </v-card>
        
          
     
            <v-subheader >参考答案</v-subheader>
            <div class="text-xs-left"> 
         
          <v-chip v-if="muqian==2||muqian==3" label v-for="(item, index) in zhsdaansx[0][muqian]">{{index+1+(muqian-2)*10}}、{{znxjoskd[item[0].zqda]}}</v-chip>
          <v-chip v-if="muqian==0||muqian==1" label v-for="(item, index) in zhsdaansx[0][muqian]">{{index+1+muqian*10}}、{{item[0].zqda}}</v-chip>
          <div  v-if="muqian>3">
          <v-chip label >{{zhsdaansx[0][4][muqian-4][0].zqda}}</v-chip>
            </br></br></br>
          </div>
            
              
               </div>
               <div v-if="muqian==2"></br></br></div>
        
        <v-subheader >批改</v-subheader>
       
    <v-layout row wrap>
      <v-flex v-if="muqian<4" xs1 v-for="item in items">
          {{item}}
        <v-checkbox color="#ad002d"  v-model="selectedxsd[muqian]" :value="item"></v-checkbox>

      </v-flex>
      <v-flex v-if="muqian>3" xs12 sm8 offset-sm2>
        </br>
          <v-text-field
            v-model="selectedxsd[muqian]"
            counter="10"
            label="本题得分"
          ></v-text-field>
        </v-flex>
    </v-layout>
     
        <v-flex xs12 sm4 offset-sm8 class="mt-2">
        <v-card-actions>
          
          
          <v-btn flat color="#181B39" @click="muqian!=0?muqian-=1:muqian=0">上一组</v-btn>
          <v-btn flat color="#181B39" @click="cidue()">{{muqian!=7?"下一组":"完成阅卷"}}</v-btn>
        </v-card-actions>
            </v-flex>
          

        </v-flex>

      </br></br>
      </v-card>
    


    </v-flex>

 
<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialogxz" scrollable max-width="400px">
      <v-card>
        <v-card-title>请选择试卷</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
          <v-radio-group v-model="dialogm1" column>
            <v-radio v-for="(item, index) in tmzl" color="#007655" :label="item.keyid" :value="index"></v-radio>
          </v-radio-group>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat="flat" @click="shijuan=tmzl[dialogm1],dialogxz = false">选择</v-btn>
          <v-btn color="green darken-1" flat="flat" @click="dialogxz = false">取消</v-btn>
        </v-card-actions>
        
      </v-card>
    </v-dialog>
  </v-layout>
</template>



<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialogzx" scrollable max-width="400px">
      <v-card>
        <v-card-title>请选择考试场次</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
          <v-radio-group v-model="dialogm2" column>
            <v-radio v-for="(item, index) in zwbzl" color="#007655" :label="item.keyname+'('+item.objectId+')'" :value="index"></v-radio>
          </v-radio-group>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat="flat" @click="kaochang=zwbzl[dialogm2],dialogzx = false">选择</v-btn>
          <v-btn color="green darken-1" flat="flat" @click="dialogzx = false">取消</v-btn>
        </v-card-actions>
        
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<template>
  <div class="text-xs-center">
    <v-dialog
      v-model="dengdai"
      hide-overlay
      persistent
      width="300"
    >
      <v-card
        color="primary"
        dark
      >
        <v-card-text>
          {{dendaish}}
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<template>
  <div class="text-xs-center">
    <v-dialog
      v-model="dialogcd"
      width="300"
    >
      

      <v-card>
        <v-card-title
          class="headline grey lighten-2"
          primary-title
        >
          成绩单
        </v-card-title>

        <v-card-text v-for="item in kaochang.zuoweib">
          姓名：{{item.name}}   成绩：{{xsdf}}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            flat
            @click="dialogcd = false"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
    
  </v-layout>
</template>

<script>
var fs=require('fs')
const dialog = require('electron').remote.dialog
export default {
  name: 'file-listing-page',
  data() {
    return {
      selectedxsd:[[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],0,0,0,0],
      dialogcd:false,
      znxjoskd:["A","B","C","D"],
      shifkaishiyj:false,
      items:[1,2,3,4,5,6,7,8,9,10],
      domotu:["https://s2.ax1x.com/2019/03/25/AthK3R.png","https://s2.ax1x.com/2019/03/25/AthK3R.png","https://s2.ax1x.com/2019/03/25/AthQjx.png","https://s2.ax1x.com/2019/03/25/AthQjx.png",
"https://s2.ax1x.com/2019/03/25/Athm4J.png",
"https://s2.ax1x.com/2019/03/25/AtheN4.png",
"https://s2.ax1x.com/2019/03/25/AthuC9.png",
"https://s2.ax1x.com/2019/03/25/AthMg1.png"],
      muqiant:["填空题(1-10)","填空题(11-20)","选择题(1-10)","选择题(11-20)","简答题1","简答题2","简答题3","简答题4"],
      muqiandan:"",
      muqian:0,
      ksyjxx:"开始阅卷",
      hover:true,
      dialogm1:0,
      dialogm2:0,
      dictorySelected: '',
      shijuan:"",
      kaochang:"",
      dengdai:false,
      dendaish:"Please stand by",
      dialogzx:false,
      dialogxz:false,
      tableData: [],
      zwbzl:[],
      tmzl:[],
      zhsdaansx:[],
      xsdf:0,
    }
  },created () {
      var shifyq=this.$db.read().get('servers').value()[0].yjqx
      this.hover=shifyq==1?true:false
    },

  methods: {
    showFileDialog() {
      dialog.showOpenDialog({ properties: ['openDirectory'] }, (filename) => {
        if (filename.length === 1) {
          this.dictorySelected = filename[0]
          console.log(this.dictorySelected)
          this.listingFile(this.dictorySelected)
        }
      })
    },
    listingFile(filepath) {
      
      const path = require('path')
      fs.readdir(filepath, (err, file) => {
        if (err) {
          
          return alert(err)
        }
        this.tableData = []
        for (let filename of file) {
          const stat = fs.statSync(path.join(filepath, filename))
          if (stat.isFile()) {
            
              this.tableData.push({
                filename: filename,
                filesize: stat.size
              })
            }
          
        }
        console.log(this.tableData)
      })
    },xuanzekaoc(){
          this.dengdai=true
          this.dendaish="正在拉取考试信息..."
          var zhendezhen=this
          this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/scan/classes/Zwbbf',
          headers: {
               "X-LC-Key": "R7K4cue4IA76BnSE6oNtCPfW,master",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          var body=JSON.parse(body).results
          console.log(body)
          zhendezhen.dengdai=false
           zhendezhen.zwbzl=body
           zhendezhen.dialogzx=true
     });
    },xuanzekaos(){
          this.dengdai=true
          this.dendaish="正在拉取题目信息..."
          var zhendezhen=this
          this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/scan/classes/Shiti',
          headers: {
               "X-LC-Key": "R7K4cue4IA76BnSE6oNtCPfW,master",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          var body=JSON.parse(body).results
          console.log(body)
          zhendezhen.dengdai=false
           zhendezhen.tmzl=body
           zhendezhen.dialogxz=true
     });
    },sliceArray(array, size) {
        
    var result = [];
    for (var x = 0; x < Math.ceil(array.length / size); x++) {
        var start = x * size;
        var end = start + size;
        result.push(array.slice(start, end));
    }
    return result;
} ,
    kaishijuejuan(){

      this.ksyjxx= this.ksyjxx=='开始阅卷'?'暂停阅卷':'开始阅卷'
      var daanx=this.shijuan.daanbh
      this.dengdai=true
      this.dendaish="正在拉取答案信息..."
      var zhenthis=this
      var zhsdaan=[[],[]]
      this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Tiku/5c95fdea12215f0072551fe5',
          headers: {
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          var body=JSON.parse(body).tiku
          for (var i=0;i<2;i++){
              for (var x=0;x<daanx[i].length;x++){
                zhsdaan[i].push(body.filter(function(elem,index,arr){
    return elem.title==daanx[i][x]
}) )

          }
    zhsdaan[i] = zhenthis.sliceArray(zhsdaan[i], 10);
          }
          zhenthis.zhsdaansx=zhsdaan
          zhenthis.shifkaishiyj=!zhenthis.shifkaishiyj
          zhenthis.dengdai=false

     });
      

      
    },cidue(){
      if(this.muqian==7){
      this.xsdf=this.selectedxsd[0].length+this.selectedxsd[1].length+this.selectedxsd[2].length*2+this.selectedxsd[3].length*2+parseInt(this.selectedxsd[4])+parseInt(this.selectedxsd[5])+parseInt(this.selectedxsd[6])+parseInt(this.selectedxsd[7])
      this.dialogcd=true}
      this.muqian!=7?this.muqian+=1:this.muqian=7
      

    }
  }
}  
  
</script>
<style>
  
</style>