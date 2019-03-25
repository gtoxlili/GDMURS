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
            v-model="shijuan"
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
            v-model="kaochang"
            append-icon="search"
            @click:append="xuanzekaoc()"
          ></v-text-field>
        </v-flex></br></br>
       <v-flex xs12 class="mt-2 ml-5">
        <v-btn class="mt-5" color="primary" dark @click="showFileDialog()">选择试卷</v-btn>
        <v-btn class="mt-5" color="primary" dark @click="ksyjxx=ksyjxx=='开始阅卷'?'结束阅卷':'开始阅卷'">{{ksyjxx}}</v-btn>
          
         </v-flex>
         </br></br></br>
      </v-layout>
    </v-container>


  </v-navigation-drawer>
</template>



</v-flex>
    <v-flex xs12 sm9>
     
     </br>   </br> 
      <v-card disabled>
        <v-toolbar flat color="translate">
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar><v-toolbar flat color="translate">
      <v-list>
        <v-list-tile>
          <v-list-tile-title class="title">
            
          </v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-toolbar>
    <v-flex xs12 sm10 offset-sm1>
        <v-img
          src="https://cdn.vuetifyjs.com/images/cards/desert.jpg"
          aspect-ratio="2.75"
        ></v-img>
      
        <v-card-title primary-title>
           <div>
            <h3 class="headline mb-0">{{muqiant[muqian]}}</h3>
            </div>
          </v-card-title>
          
     
            <v-subheader >答案</v-subheader>
            <div class="text-xs-center"> 
             
          <v-chip label v-for="item in items">{{item}}、A</v-chip>
       

    
              
               </div>
        
        <v-subheader >批改</v-subheader>
       
    <v-layout row wrap>
      <v-flex xs1 v-for="item in items">
          {{item}}
        <v-checkbox color="#ad002d" indeterminate></v-checkbox>

      </v-flex>
    </v-layout>

        <v-flex xs12 sm4 offset-sm8>
        <v-card-actions>
          
          <v-btn flat color="#007f89">保存进度</v-btn>
          
          <v-btn flat color="#181B39">下一组</v-btn>
        </v-card-actions>
            </v-flex>
          

        </v-flex>
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
          <v-btn color="green darken-1" flat="flat" @click="shijuan=tmzl[dialogm1].keyid,dialogxz = false">选择</v-btn>
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
          <v-btn color="green darken-1" flat="flat" @click="kaochang=zwbzl[dialogm2].objectId,dialogzx = false">选择</v-btn>
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

    
  </v-layout>
</template>

<script>
var fs=require('fs')
const dialog = require('electron').remote.dialog
export default {
  name: 'file-listing-page',
  data() {
    return {
      items:[1,2,3,4,5,6,7,8,9,10,11,12],
      muqiant:["选择题","填空题","简答题"],
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
      isLoading: false,
      dialogzx:false,
      dialogxz:false,
      tableData: [],
      zwbzl:[],
      tmzl:[]
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
          this.listingFile(this.dictorySelected)
        }
      })
    },
    listingFile(filepath) {
      this.isLoading = true
      const path = require('path')
      fs.readdir(filepath, (err, file) => {
        if (err) {
          this.isLoading = false
          return alert(err)
        }
        this.tableData = []
        for (let filename of file) {
          const stat = fs.statSync(path.join(filepath, filename))
          if (stat.isFile()) {
            if (path.extname(filename).toLowerCase() === '.md') {
              this.tableData.push({
                filename: filename,
                filesize: stat.size
              })
            }
          }
        }
        this.isLoading = false
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
    }
  }
}  
  
</script>
<style>
  
</style>