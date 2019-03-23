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
          <v-checkbox v-model="hover" disabled label="管理题库权限" hide-details></v-checkbox>
        </v-flex>
        <v-flex xs12 class="mt-2 ml-3">
          <v-subheader>题型</v-subheader>
          <v-radio-group v-model="xaixtx" hide-details>
            <v-radio value="全部" label="全部"></v-radio>
            <v-radio value="选" label="选择题"></v-radio>
            <v-radio value="填" label="填空题"></v-radio>
            <v-radio value="简" label="简答题"></v-radio>
          </v-radio-group>
        </v-flex>
        <v-flex xs12 class="mt-2 ml-3">
          <v-subheader>难度</v-subheader>
          <v-radio-group v-model="xaixnd" hide-details>
            <v-radio value="全部" label="全部"></v-radio>
            <v-radio value="1" label="⭐"></v-radio>
            <v-radio value="2" label="⭐⭐"></v-radio>
            <v-radio value="3" label="⭐⭐⭐"></v-radio>
            <v-radio value="4" label="⭐⭐⭐⭐"></v-radio>

          </v-radio-group>
        </v-flex>
       <v-flex xs12 class="mt-2 ml-3">
        <v-btn class="mt-5"  :disabled="!hover" color="primary" dark @click="window=true">生成试卷</v-btn>
          
         </v-flex>
      </v-layout>
    </v-container>


  </v-navigation-drawer>
</template>



</v-flex>
    <v-flex xs12 sm9>
      <v-card>
        
        <v-toolbar color="cyan" dark>
          <v-toolbar-side-icon></v-toolbar-side-icon>

          <v-toolbar-title>Inbox</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-btn icon>
            <v-icon>search</v-icon>
          </v-btn>
        </v-toolbar>
        <v-list class="mt-2" two-line subheader>
          <v-subheader
              :key="'试题集'"
            >
              试题集
            </v-subheader>
          <template v-for="(item, index) in items">
            
          
            <v-list-tile
              :key="item.title"
              avatar
              @click="editItem(item)"
            >
              <v-list-tile-avatar>
                <v-chip :color="yanse[item.avatar]" label text-color="white">{{item.avatar}}</v-chip>
              </v-list-tile-avatar>
      
              <v-list-tile-content>
                <v-list-tile-title v-html="item.title"></v-list-tile-title>
                <v-list-tile-sub-title v-html="item.subtitle"></v-list-tile-sub-title>
              </v-list-tile-content>
              <v-list-tile-avatar>
                <v-btn fab dark flat small color="#3f485b" v-if="hover==true" @click="deleteItem(item)">
      <v-icon dark>close</v-icon>
    </v-btn>
              </v-list-tile-avatar>
            </v-list-tile>
            <v-divider
              v-if="!item.header"
              :key="index"
              inset
            ></v-divider>
          </template>
        </v-list>
      </v-card>
       <template>
  <v-layout row justify-center>
    <v-dialog v-model="window" max-width="290">
      <v-card>
        <v-card-title class="headline">确定生成试卷</v-card-title>
        <v-card-text>请稍等片刻后</br>通过软件根目录获取试卷</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click="shengcshij()">agree</v-btn>
          </v-card-actions>
          <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-2" flat @click="window = false">DISAgree</v-btn>
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
    </v-flex>

 <v-dialog v-model="dialog" max-width="500px">
      
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                
                  <v-radio-group v-model="editedItem.avatar" row>
                    <v-flex xs12 sm4 md4>
      <v-radio label="选择题" value="选"></v-radio>
</v-flex>
                  <v-flex xs12 sm4 md4>
      <v-radio label="填空题" value="填"></v-radio>
                    </v-flex>
                  <v-flex xs12 sm4 md4>
      <v-radio label="简答题" value="简"></v-radio>
      </v-flex>
    </v-radio-group>
                
               
                <v-flex xs12>
                  <v-textarea
                  counter
          name="input-7-1"
          label="题目"
          v-model="editedItem.subtitle"
        ></v-textarea>
                </v-flex>


                <template v-if="editedItem.avatar!='简'">
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.nd" label="难度" hint="(1-4星)"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.dzsj" label="大致所需时间" hint="(min)"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.zqda" label="正确答案"></v-text-field>
                </v-flex>
                  <template v-if="editedItem.avatar=='选'">
                    <v-flex xs12>
                    
        
     
      <p class="text-md-left">答案选项</p>
                    </v-flex>  
                  <v-flex xs12 sm6 md3>
                  <v-text-field v-model="editedItem.daan[0]" label="A选项"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md3>
                  <v-text-field v-model="editedItem.daan[1]" label="B选项"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md3>
                  <v-text-field v-model="editedItem.daan[2]" label="C选项"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md3>
                  <v-text-field v-model="editedItem.daan[3]" label="D选项"></v-text-field>
                </v-flex>
                


                 </template>

                </template>


                <template v-else>
                <v-flex xs12 sm6 md6>
                  <v-text-field v-model="editedItem.nd" label="难度" hint="(1-4星)"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md6>
                  <v-text-field v-model="editedItem.dzsj" label="大致所需时间" hint="(min)"></v-text-field>
                </v-flex>
                <v-flex xs12>
                 <v-textarea
                 counter
                 v-model="editedItem.zqda"
          name="input-7-1"
          label="答案"
          hint="Hint text"
        ></v-textarea>
                </v-flex>
                </template>


              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
            <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>



  <floatbottom v-if="hover==true" v-on:childByValue="childByValue"></floatbottom>
    
  </v-layout>
</template>

<script>
var fs=require('fs')
import floatbottom from "./floatbottom"
var iconv = require('iconv-lite');
import { remote } from 'electron';
const { shell } = require('electron')
  export default {
     components: {
    floatbottom
  },
    data () {
      return {
        xaixtx:"全部",
        xaixnd:"全部",
        dengdai:false,
        dialog:false,
        dendaish:"Please stand by",
        window: false,
        hover:true,
        right: null,
        editedIndex: -1,
        defaultItem: {
        "nd": "",
        "daan": [
            "",
            "",
            "",
            ""
        ],
        "title": "",
        "subtitle": "",
        "avatar": "",
        "dzsj": "",
        "zqda": ""
    },
        editedItem: {
        "nd": "",
        "daan": [
            "",
            "",
            "",
            ""
        ],
        "title": "",
        "subtitle": "",
        "avatar": "",
        "dzsj": "",
        "zqda": ""
    },
        yanse:{"选":"#db3a34","填":"#084c61","简":"#177e89"},
        items: [
        ]
      }
    },computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Problem' : 'Edit Problem'
      }
    },
    
    
    watch: {
      xaixtx (val) {
        this.shaixuan(val)
      },
      xaixnd (val) {
        this.shaixuannd(val)
      }
    }
    
    
    
    ,created () {
      var shifyq=this.$db.read().get('servers').value()[0].tkqx
      this.hover=shifyq==1?true:false
      this.huoqujson()
    },methods: {
      mySetTimeout(ms) {
    var currentTime = new Date().getTime();
    while (new Date().getTime() < currentTime + ms);
},
      luanxu(shuzu){
    var input = shuzu;
    for (var i = input.length-1; i >=0; i--) {
        var randomIndex = Math.floor(Math.random()*(i+1)); 
        var itemAtIndex = input[randomIndex]; 
        input[randomIndex] = input[i]; 
        input[i] = itemAtIndex;
    }
    return input;
},

      huoqujson(){
        try{
          let result = JSON.parse(fs.readFileSync(remote.app.getPath("home")+"/tiku/tiku.json").toString().replace(/\s+/g,""))
          this.items=result
          }
        catch(err)
  {    
        fs.mkdirSync(remote.app.getPath("home")+"/tiku")
        fs.mkdirSync(remote.app.getPath("home")+"/tiku/shijuan")
  }
          

      },shaixuan(xecs){
          let result = JSON.parse(fs.readFileSync(remote.app.getPath("home")+"/tiku/tiku.json").toString().replace(/\s+/g,""));
          var xsdf=[]
          if(xecs!="全部"){
    for (var x = 0; x < result.length; x++) {
        if (result[x].avatar==xecs){
          xsdf.push(result[x])
        }
    }
        this.items=xsdf}
        else{
          this.items=result
        }

      },shaixuannd(xecs){
          let result = JSON.parse(fs.readFileSync(remote.app.getPath("home")+"/tiku/tiku.json").toString().replace(/\s+/g,""));
          var xsdf=[]
          if(xecs!="全部"){
    for (var x = 0; x < result.length; x++) {
        if (result[x].nd==xecs){
          xsdf.push(result[x])
        }
    }
        this.items=xsdf}
        else{
          this.items=result
        }

      }  ,childByValue: function (childValue) {
        console.log(childValue)
        // childValue就是子组件传过来的值
        if(childValue=="attach_file"){
            this.attach_file()
        }else if(childValue=="add"){
            this.dialog = true
        }else if(childValue=="cloud_upload"){
          this.cloud_upload()
        }else{
          this.cloud_download()
        }
      },
      attach_file(){
        console.log("ydk")
          shell.showItemInFolder(remote.app.getPath("home")+"/tiku/tiku.json")
      },cloud_upload(){
        this.dendaish="正在上传题库，请稍等。"
          var zhesthis=this
          this.dengdai=true
          this.$http({
          method: 'PUT',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Tiku/5c95fdea12215f0072551fe5',
          json: true,
          headers: {
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
               "Content-Type": "application/json"
          },
          body: {
               "tiku":zhesthis.items
          }
     }, function (err, res, body) {
          console.log(body)
          zhesthis.dengdai=false
          
     });

      },cloud_download(){
        this.dendaish="正在下载题库，请稍等。"
          this.dengdai=true
          var zhesthis=this
          this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Tiku/5c95fdea12215f0072551fe5',
          headers: {
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          var body=JSON.parse(body).tiku
          fs.writeFileSync(remote.app.getPath("home")+"/tiku/tiku.json", JSON.stringify(body), 'utf8');
          zhesthis.items=body
          zhesthis.dengdai=false
     });





      },editItem (item) {
        this.editedIndex = this.items.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },deleteItem (item) {
        const index = this.items.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.items.splice(index, 1)
        fs.writeFileSync(remote.app.getPath("home")+"/tiku/tiku.json", JSON.stringify(this.items), 'utf8');
      },close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },save () {
        this.editedItem.title="编号："+(this.items.length+1).toString()
        if (this.editedIndex > -1) {
          
          Object.assign(this.items[this.editedIndex], this.editedItem)
          fs.writeFileSync(remote.app.getPath("home")+"/tiku/tiku.json", JSON.stringify(this.items), 'utf8');
        } else {

          this.items.push(this.editedItem)
          fs.writeFileSync(remote.app.getPath("home")+"/tiku/tiku.json", JSON.stringify(this.items), 'utf8');
        }
        this.close()
      },shengcshij(){
          this.dengdai=true
          this.window=false
          var today = new Date();
          var xsxsxsxs=["A","B"]
          this.dendaish="正在拉取题库..."
          var xsidzhen=this
          setTimeout(function(){
var shijbf={"keyid":today.getFullYear().toString()+(today.getMonth().length==2?today.getMonth()+1:"0"+(today.getMonth()+1))+today.getDate().toString(),"daanbh":[[],[]]}

for (var xsxsx=0;xsxsx<2;xsxsx++){
          
         
          
          let resulxst = fs.readFileSync(remote.app.getPath("home")+"/tiku/st.htm")
          var daichuli=iconv.decode(resulxst, 'gbk').split("zhelichatiaaaaaaaaaaaaaaa")
          daichuli[0]=daichuli[0]+xsxsxsxs[xsxsx]+"("+shijbf.keyid+")"
          xsidzhen.shaixuan("填")
          
          var daixhtk=xsidzhen.luanxu(xsidzhen.items)
          for (var i=0;i<daixhtk.length;i++){
                  shijbf.daanbh[xsxsx].push(daixhtk[i].title)
                  daichuli[1]=daichuli[1]+`<p class=MsoNormal style='line-height:150%'><span lang=EN-US style='font-family:宋体'>`+(i+1)+`</span><span style='font-family:宋体'>、`+daixhtk[i].subtitle+`</span></p>`
          }
          xsidzhen.shaixuan("选")
          
          daixhtk=xsidzhen.luanxu(xsidzhen.items)
          for (var i=0;i<daixhtk.length;i++){
            shijbf.daanbh[xsxsx].push(daixhtk[i].title)
                  daichuli[2]=daichuli[2]+`<p class=MsoNormal style='line-height:150%'><span lang=EN-US style='line-height:
150%;font-family:宋体;letter-spacing:.25pt'>(&nbsp;&nbsp; )`+(i+1)+`.</span><span
lang=EN-US> </span><span style='line-height:150%;font-family:宋体;letter-spacing:
.25pt'>`+daixhtk[i].subtitle+`</span></p>

<p class=MsoNormal style='margin-left:19.5pt;text-indent:3.0pt;line-height:
150%'><span lang=EN-US style='line-height:150%;font-family:宋体;letter-spacing:
.25pt'>A. </span><span style='line-height:150%;font-family:宋体;letter-spacing:
.25pt'>`+daixhtk[i].daan[0]+`</span></p>

<p class=MsoNormal style='text-indent:22.5pt;line-height:150%'><span
lang=EN-US style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>B. </span><span
style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>`+daixhtk[i].daan[1]+`</span></p>

<p class=MsoNormal style='text-indent:16.5pt;line-height:150%'><span
lang=EN-US style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>&nbsp;C.
</span><span style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>`+daixhtk[i].daan[2]+`</span></p>

<p class=MsoNormal style='text-indent:22.0pt;line-height:150%'><span
lang=EN-US style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>D. </span><span
style='line-height:150%;font-family:宋体;letter-spacing:.25pt'>`+daixhtk[i].daan[3]+`</span></p>`
          }
          xsidzhen.shaixuan("简")
        
          daixhtk=xsidzhen.luanxu(xsidzhen.items)
          for (var i=0;i<4;i++){
            shijbf.daanbh[xsxsx].push(daixhtk[i].title)
                  daichuli[3]=daichuli[3]+`<p class=MsoNormal style='line-height:150%'><span lang=EN-US style='font-family:
宋体'>`+(i+1)+`</span><span style='font-family:宋体'>、`+daixhtk[i].subtitle+`（<span
lang=EN-US>10</span>分）</span></p>

<p style='margin:0cm;margin-bottom:.0001pt;layout-grid-mode:char'><span
lang=EN-US style='font-size:10.5pt'>&nbsp;</span></p>

<p style='margin:0cm;margin-bottom:.0001pt;layout-grid-mode:char'><span
lang=EN-US style='font-size:10.5pt'>&nbsp;</span></p>

<p style='margin:0cm;margin-bottom:.0001pt;layout-grid-mode:char'><span
lang=EN-US style='font-size:10.5pt'>&nbsp;</span></p>`
          }
          
          fs.writeFileSync(remote.app.getPath("home")+"/tiku/shijuan/"+xsxsxsxs[xsxsx]+"卷.html", iconv.encode(daichuli.join(""), 'gbk'));
          
}
xsidzhen.dendaish="正在上传试卷..."
xsidzhen.$http({
          method: 'POST',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Shiti',
          json: true,
          headers: {
               "Content-Type": "application/json",
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }, body: shijbf
     }, function (err, res, body) {
          console.log(body)
          xsidzhen.dengdai=false
xsidzhen.shaixuan("全部")
shell.showItemInFolder(remote.app.getPath("home")+"/tiku/shijuan/A卷.html")
     });





},3000)

      }


    }
  }
</script>
<style>
  
</style>