<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3 >
      <v-card class="card--flex-toolbar">
        <v-img
          src='https://s2.ax1x.com/2019/03/18/AnEMbq.jpg'
          aspect-ratio="2.75"
        ></v-img>

      
 <template>
  <v-layout
    column
    justify-center
  >
    <v-subheader>广东医科大学</v-subheader>

    <v-expansion-panel popout>
      <v-expansion-panel-content
        v-for="(message, i) in messages"
        :key="i"
        hide-actions
      >
        <template v-slot:header>
          <v-layout
            align-center
            row
            spacer
          >
            <v-flex xs4 sm2 md1>
              <v-avatar
                size="26px"
              >
                <img
                  v-if="message.avatar"
                  src='./touxiang.jpg'
                  alt="Avatar"
                >
                <v-icon
                  v-else
                  :color="message.color"
                  v-text="message.icon"
                ></v-icon>
              </v-avatar>
            </v-flex>

            <v-flex sm5 md3 hidden-xs-only>
              <strong v-html="message.name"></strong>
              <span
                v-if="message.total"
                class="grey--text"
              >
                &nbsp;({{ message.total }})
              </span>
            </v-flex>

            <v-flex no-wrap xs5 sm3>
              <v-chip
                v-if="message.new"
                :color="`${message.color} lighten-4`"
                class="ml-0"
                label
                small
              >
                {{ message.new }} new
              </v-chip>
              <strong v-html="message.title"></strong>
            </v-flex>

            
          </v-layout>
        </template>

        <v-card>
          <v-divider></v-divider>
          <div v-if="message.title==='开发者'"> 
          <v-card-text v-text="'感谢使用我的软件，可通过下列联系方式进行问题反馈：'"></v-card-text>
          <template>
          
  <div class="text-xs-left mb-2 ml-3">
    <v-chip @click="See('https://github.com/Glovecc')" label outline color="#084c61">Github</v-chip>
    <v-chip @click="See('mailto:gtcc1108@gmail.com')" label outline color="#177e89">Email</v-chip>
    <v-chip @click="See('https://juniancc.club')" label outline color="#db3a34">Blog</v-chip>
  </div>
</template>
        </div>
        <div v-else-if="message.title==='当前管理员个人信息'">
          <v-card-text class="ml-3">姓名： {{grenxs[0]}}</br>管理员ID： {{grenxs[1]}}</br>管理员权限： {{grenxs[2]}} {{grenxs[3]}}</v-card-text>
          <div class="text-xs-left mb-2 ml-3">
    <v-chip @click="dialogxwxwx()" label outline color="#373c38">管理下级用户</v-chip>
    <v-chip @click="gaimima=true" label outline color="#43341b">更改密码</v-chip>
  </div>
          </div>
          <div v-else>
            <v-card-text class="ml-2" v-text="lorem"></v-card-text>
            </div>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-layout>
</template>


       <v-card-actions >
          <div class="text-xs-center ml-2">
          
          <v-chip :value="!zhuce" @click="dialog=true" light label color="pink" text-color="white">
      <v-icon left>label</v-icon>新增管理员
    </v-chip>
     <v-chip @click="exitdl()" light label color="#0d1130" text-color="white">
      <v-icon left>exit_to_app</v-icon>退出登录
    </v-chip>
        <v-chip label disabled>软件设计大赛橘年队</v-chip>
     

          
          </div>
        </v-card-actions>
      </v-card>
    </v-flex>


    <template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="600px">
      
      <v-card>
        <v-card-title>
          <span class="headline">新增管理员</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 sm6 >
                <v-text-field v-model="shouquanx[0]" label="账号*" required></v-text-field>
              </v-flex>
              <v-flex xs12 sm6 >


                <v-text-field
            v-model="shouquanx[1]"
            :append-icon="show1 ? 'visibility' : 'visibility_off'"
            :type="show1 ? 'text' : 'password'"
            label="密码*"
            required
            counter
            @click:append="show1 = !show1"
          ></v-text-field>


              </v-flex>
              
              <v-flex xs12>
                <v-text-field v-model="shouquanx[2]" label="呢称*" required></v-text-field>
              </v-flex>
            
               <v-flex xs12>
     
      <p class="text-md-left">Authority management</p>
     
   </v-flex>
              
              <v-flex xs12 sm6>
                
              <v-checkbox
              :disabled="grenxs[3]==''"
              v-model="quanxianlr[1]"
              label="题库管理"
              color="#0086a2"
           
              hide-details
            ></v-checkbox>
              
              </v-flex>
              <v-flex xs12 sm6>
               <v-checkbox
               :disabled="grenxs[2]==''"
              v-model="quanxianlr[0]"
              label="改卷权限"
              color="#0086a2"

              hide-details
            ></v-checkbox>

              </v-flex>
          
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" flat @click="dialog = false">关闭</v-btn>
          <v-btn :disabled="shouquanx[0]==''||shouquanx[1]==''||shouquanx[2]==''" color="blue darken-1" flat @click="shouquan()">注册</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialogxwxf" scrollable max-width="300px">
      <v-card>
        <v-card-title>权限修改</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 150px;">
          <v-checkbox
              :disabled="grenxs[3]==''"
         
              label="题库管理"
              color="#0086a2"
           
              hide-details
            ></v-checkbox>
    
            
               <v-checkbox
               :disabled="grenxs[2]==''"
            
              label="改卷权限"
              color="#0086a2"

              hide-details
            ></v-checkbox>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat="flat" @click="dialogxwxf=false">取消</v-btn>
          <v-btn color="green darken-1" flat="flat" @click="dialogxwxf=false">确定</v-btn>
        </v-card-actions>
        
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialogxwxwxw" scrollable max-width="400px">
      <v-card>
        <v-card-title>管理下级用户</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;">
          <v-radio-group v-model="dialogm1" column>
            <v-radio v-for="(item, index) in zwbzl" color="#007655" :label="item.xinmin+'('+item.login+')'" :value="index"></v-radio>
          </v-radio-group>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat="flat" @click="shanchuuser()">删除</v-btn>
          <v-btn color="green darken-1" flat="flat" @click="dialogxwxwxw = false,dialogxwxf=true">更改权限</v-btn>
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
          Please stand by
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
  <v-layout row justify-center>
    <v-dialog overlay v-model="gaimima" max-width="400px">

   <v-card class="elevation-12">
              <v-card-title>
          <span class="headline">更改密码</span>
        </v-card-title>
              <v-card-text>
                <v-form>
                  <v-text-field
            v-model="gaimimas[0]"
            :append-icon="show2 ? 'visibility' : 'visibility_off'"
            :type="show2 ? 'text' : 'password'"
            label="旧密码*"
            required
            counter
            @click:append="show2 = !show2"
          ></v-text-field><v-text-field
            v-model="gaimimas[1]"
            :append-icon="show3 ? 'visibility' : 'visibility_off'"
            :type="show3 ? 'text' : 'password'"
            label="新密码*"
            required
            counter
            @click:append="show3 = !show3"
          ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled='gaimimas[1]==""||gaimimas[0]!=password' color="blue darken-1" flat @click=" gaimimaxs()">Change</v-btn>
              </v-card-actions>
            </v-card>

    </v-dialog>
  </v-layout>
</template>


<template>
  <v-layout row justify-center>
    <v-dialog overlay v-model="zhuce" persistent max-width="400px">

   <v-card class="elevation-12">
              <v-toolbar dark color="#000b00">
                <v-toolbar-title>登录</v-toolbar-title>
    
                <v-tooltip right>
                  
                  <span>Codepen</span>
                </v-tooltip>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field prepend-icon="person" v-model="login" label="Login" type="text"></v-text-field>
                  <v-text-field id="password" prepend-icon="lock" v-model="password" label="Password" counter type="password"></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn :disabled='login==""||password==""' dark color="#000b00" @click=" zhuces()">Login</v-btn>
              </v-card-actions>
            </v-card>

    </v-dialog>
  </v-layout>
</template>

<v-snackbar
      v-model="snackbar"
      color="error"
      bottom
      multi-line
  
    >
      {{ snackbartext }}
      <v-btn
        dark
        flat
        color="pink"
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>


  </v-layout>

</template>

<script>

  export default {
    data: () => ({
      dialogm1:0,
      zwbzl:[],
      dengdai:false,
      dialogxwxwxw:false,
      gaimima:false,
      gaimimas:["",""],
      snackbar:false,
      snackbartext:"",
      dialogxwxf:false,
      show1: false,
      show2: false,
      show3: false,
      login:"",
      password:"",
      drawer: null,
      zhuce:false,
      dialog: false,
      shouquanx:["","",""],
      quanxianlr:[false,false],
      grenxs:[
        "","","",""
      ],
      messages: [
        {
          avatar: 'touxiang.jpg',
          name: 'Ju nian',
          title: '开发者',
        },
        {
          color: 'red',
          icon: 'people',
          name: '管理员',
          new: 1,
          total: 1,
          title: '当前管理员个人信息'
        },
        {
          color: 'teal',
          icon: 'local_offer',
          name: '通知',
          new: 2,
          total: 4,
          title: '消息提示',
          exceprt: 'New deals available, Join Today'
        }
      ],
      lorem: 'coming soon......'
    }),
    methods:{shouquan(){
          this.dengdai=true
          this.dialog = false
        var txwxwsd=this
          this.$http({
          method: 'POST',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Userws',
          json: true,
          headers: {
               "Content-Type": "application/json",
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }, body: {
               "login":txwxwsd.shouquanx[0],"password":txwxwsd.shouquanx[1],"xinmin":txwxwsd.shouquanx[2],"yjqx":txwxwsd.quanxianlr[0]?1:0,"tkqx":txwxwsd.quanxianlr[1]?1:0,"shangjis":txwxwsd.grenxs[0]
          }
     }, function (err, res, body) {
          console.log(body)

          txwxwsd.dengdai = false
          txwxwsd.snackbar=true
                txwxwsd.snackbartext="用户"+txwxwsd.shouquanx[2]+",已授权。"
     });

    },
     
    
    See(e){

      this.$electron.shell.openExternal(e);
    },exitdl(){

      this.$db.get('servers')
  .remove({ type: '当前用户' })
  .write()
this.zhuce = true
    }
    ,
    zhuces(){
      var truets=this
     
      this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/scan/classes/Userws?where={"login": "'+truets.login+'"}',
          headers: {
               "X-LC-Key": "R7K4cue4IA76BnSE6oNtCPfW,master",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          var body=JSON.parse(body).results
          console.log(body)
          if(body.length!=0){
            var body=body[0]
            if(body.login==truets.login && body.password==truets.password){


                truets.$db.get('servers')
  .push({
  type:"当前用户", // 对数组进行insert操作
  title:body.login,
  content: body.password,
  xinmin: body.xinmin,
  objid:body.objectId,
  yjqx:body.yjqx,
  tkqx:body.tkqx

}).write()

truets.login=body.login
truets.password= body.password
truets.grenxs=[body.xinmin,body.objectId,body.yjqx==1?"阅卷":"",body.tkqx==1?"题库管理":""]
truets.zhuce = false
truets.snackbar=true
truets.snackbartext="用户:"+body.xinmin+",欢迎回家"
console.log(truets.$db.read().get('servers').value())


            }else{

               
                truets.snackbar=true
                truets.snackbartext="用户账号密码错误"
                // 用户账号密码错误

            }
          }else{
              truets.snackbar=true
                truets.snackbartext="此用户名不存在"
            // 此用户不存在

          }
          
     });
      
    
    
    },gaimimaxs(){
          this.gaimima=false
          this.dengdai=true
          var zhenthis=this
          this.$http({
          method: 'PUT',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Userws/'+zhenthis.grenxs[1],
          json: true,
          headers: {
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
               "Content-Type": "application/json"
          },
          body: {
               "password":zhenthis.gaimimas[1]
          }
     }, function (err, res, body) {
          console.log(body)
          zhenthis.dengdai=false
          zhenthis.snackbar=true
          zhenthis.snackbartext="用户密码更改成功"
          
     });





    },dialogxwxwx(){
        this.dengdai=true
        var txwxwsd=this
       
        this.$http({
          method: 'GET',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/scan/classes/Userws?where={"shangjis": "'+encodeURI(txwxwsd.grenxs[0])+'"}',
          headers: {
               "X-LC-Key": "R7K4cue4IA76BnSE6oNtCPfW,master",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {

          var body=JSON.parse(body).results
          console.log(body)
          txwxwsd.dengdai=false
         txwxwsd.dialogxwxwxw=true
          txwxwsd.zwbzl=body
     });


    },shanchuuser(){
        this.dialogxwxwxw=false
        this.dengdai=true
        var xsthis=this
        var daishancu=this.zwbzl[this.dialogm1]
        this.$http({
          method: 'DELETE',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Userws/'+daishancu.objectId,
          headers: {
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }
     }, function (err, res, body) {
          console.log(body)
          xsthis.dengdai=false
          xsthis.snackbar=true
          xsthis.snackbartext="用户"+daishancu.xinmin+"，已删除。"
          
     });

    }
    },created:function (){
    

      if(this.$db.read().get('servers').value()==undefined){
        this.$db.defaults({
	servers: []
}).write()}


if (this.$db.read().get('servers').value()[0]==undefined){
  
  this.zhuce=true;
}else{
  var gerenxx=this.$db.read().get('servers').value()[0]
  console.log(gerenxx)
  this.login=gerenxx.title
  this.password=gerenxx.content
  this.grenxs=[gerenxx.xinmin,gerenxx.objid,gerenxx.yjqx==1?"阅卷":"",gerenxx.tkqx==1?"题库管理":""]
  this.zhuce=false;
}


    }
      
  }
</script>
<style>

   .card--flex-toolbar {
    margin-top: 125px;
  }
  .text-wrapper {
  white-space: pre-wrap;
  text-align:left;
}
</style>
