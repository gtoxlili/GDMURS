<template>
  <v-layout row>
     <v-flex xs12 sm3>
    <template>
  <v-navigation-drawer permanent class="mt-0">
    <v-toolbar flat>
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
        <v-flex xs12 >
          <v-subheader >Options</v-subheader>
         <template>
  <v-form>
    <v-container>
      <v-layout  row  wrap>
      
          <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[0]" clearable mask=###########-########### return-masked-value prop
            label="请输入起止学号"
          ></v-text-field>
        </v-flex>
          <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[1]" clearable mask=A#-# return-masked-value prop
            label="请输入考场"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[2]" clearable
            label="请输入考试科目"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[3]" clearable mask=####级 return-masked-value prop
            label="请输入年级"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[4]" clearable mask=####-##-## return-masked-value prop
            label="请输入考试日期"
          ></v-text-field>
        </v-flex>
        <v-flex xs12>
          <v-text-field flat v-model="zuoweibxx[5]" clearable mask=##:##-##:## return-masked-value prop
            label="请输入考试时间"
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>
        </v-flex>
       <v-flex xs12 class="mt-1 ml-3">
        <v-btn class="mt-0" color="primary" :disabled="zuoweibxx[0]==''" dark @click="sczuoweibyp()">生成座位表样品</v-btn>

          <v-btn class="mt-3" :disabled="!havefb" color="primary" dark @click="window=true">生成座位表成品</v-btn>
         </v-flex>
      </v-layout>
    </v-container>


  </v-navigation-drawer>
</template>



</v-flex>
    <v-flex xs12 sm9>
        <template>
  <v-layout row>
    <v-flex xs12>
      <v-card class="card--flex-tor">
        <v-toolbar color="white" dark>
      


        </v-toolbar>
        <template>
  <div>
    <v-toolbar flat color="white">
      <v-subheader>座位表样品</v-subheader>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
     
          <v-btn color="primary" dark class="mb-2" @click="editItem('')">New Item</v-btn>
        
    </v-toolbar>




  <v-container grid-list-md text-xs-left>
    <v-layout row wrap>
      
      <v-flex v-for="i in exevls" xs4>
       
          {{i}}
        
      
      </v-flex>
    </v-layout>
  </v-container>

    <v-data-table
      rows-per-page-text=""
      :headers="headers"
      :items="desserts"
      class="elevation-1"
      :pagination.sync="pagination"
    >
      <template v-slot:items="props">
        <td>{{ props.item.name }}</td>
        
        <td class="text-xs-left">{{ props.item.fat }}</td>
        
        <td class="text-xs-left">{{ props.item.protein }}</td>
        <td class="justify-center layout mr-5 px-0">
          <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          >
            edit
          </v-icon>
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            delete
          </v-icon>
        </td>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>


      </v-card>
    </v-flex>
  </v-layout>
</template>


       <v-dialog v-model="dialog" max-width="500px">
      
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.name" label="考生名称"></v-text-field>
                </v-flex>
               
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.fat" label="学号"></v-text-field>
                </v-flex>
                
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.protein" label="座位号"></v-text-field>
                </v-flex>
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


       <template>
  <v-layout row justify-center>
    <v-dialog v-model="window" max-width="290">
      <v-card>
        <v-card-title class="headline">确定生成座位表</v-card-title>
        <v-flex xs12 sm8 offset-md1>
          <v-text-field flat v-model="zuoweibminz" clearable hint="名字请尽量特征化"
            label="座位表名称"
          ></v-text-field>
        </v-flex>
        
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" :disabled="zuoweibminz==''" flat @click=" sczuoweicp() ">agree</v-btn>
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
    </v-flex>

<v-snackbar
      v-model="snackbar"
      color="#00081A"
      bottom
      multi-line
  
    >
      {{ snackbartext }}
      <v-btn
        dark
        flat
        color="pink"
        @click="openfile()"
      >
        OPEN
      </v-btn>
    </v-snackbar>

  </v-layout>
</template>

<script>
import { remote } from 'electron';
import Excel from 'exceljs';
const { shell } = require('electron')
  export default {
    data () {
      return {
        snackbartext:"",
        snackbar:false,
        zuoweibminz:"",
        zuoweibxx:["","","","","",""],
        dialog: false,
        pagination:{
          rowsPerPage:8
        },
      headers: [
        {
          text: '考生名称',
          align: 'left',
          sortable: true,
          value: 'name'
        },
        { text: "学号", value: 'fat' },
        { text: '座位号', value: 'protein' },
        { text: 'Actions', value: 'name', sortable: false }
      ],
      desserts: [{}],
      editedIndex: -1,
      editedItem: {
        name: '',
        fat: 0,
        protein: 0
      },
      defaultItem: {
        name: '',
        fat: 0,
        protein: 0
      },
        havefb:false,
        dengdai:false,
        window: false,
        exevls:[],
      }
    },computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      }
    },

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      console.log(this.$db.read().get('zuowei').value())
      this.initialize()
    },

    methods: {
      sliceArray(array, size) {
        
    var result = [];
    for (var x = 0; x < Math.ceil(array.length / size); x++) {
        var start = x * size;
        var end = start + size;
        result.push(array.slice(start, end));
    }
    return result;
} ,
      sczuoweicp(){
          var zhendsss=this
          this.window = false
          this.dengdai=true
          var workbook = new Excel.Workbook();
          var sheet = workbook.addWorksheet('My Sheet');
          var dakey=["name","fat","protein"]
          var dataxsx = this.sliceArray(this.desserts, 4);
          console.log(dataxsx)
          sheet.addRow();
          sheet.mergeCells('A2:L2');
          sheet.getCell('A2').value = '广东医科大学学生考试编号表';
          sheet.findRow(2).alignment = { vertical: 'middle', horizontal: 'center' };
          sheet.mergeCells('A3:D3')
          sheet.getCell('A3').value = this.exevls[1]
          sheet.mergeCells('E3:H3')
          sheet.getCell('E3').value = this.exevls[3]
          sheet.mergeCells('I3:L3')
          sheet.getCell('I3').value = this.exevls[0]
          sheet.mergeCells('A4:D4')
          sheet.getCell('A4').value = this.exevls[2]
          sheet.mergeCells('E4:H4')
          sheet.getCell('E4').value = this.exevls[4]
          sheet.mergeCells('I4:L4')
          sheet.getCell('I4').value = this.exevls[5]
          sheet.addRow(["座位表","姓名","学号","座位表","姓名","学号","座位表","姓名","学号","座位表","姓名","学号"]);
          var xiuds=0
          for(let i =0;i<dataxsx.length;i++){
              var axa=[]
              for(let k =0;k<dataxsx[i].length;k++){
                  axa=axa.concat(Object.values(dataxsx[i][k]))

              }
              sheet.addRow(axa);
              xiuds+=1
              }
          for(let i = 2; i <= 5+xiuds; i++) {
                  sheet.findRow(i).alignment = { vertical: 'middle', horizontal: 'center' };
                  //循环 row 中的　cell，给每个 cell添加边框
                  sheet.findRow(i).eachCell(function (cell, index) {
                      cell.border = {
                          top: {style:'thin'},
                          left: {style:'thin'},
                          bottom: {style:'thin'},
                          right: {style:'thin'}
                      };
                  })

              }
          workbook.xlsx.writeFile(remote.app.getPath("desktop")+"/座位表.xlsx")//将workbook生成文件
              .then(function() {

    

          zhendsss.$http({
          method: 'POST',
          url: 'https://tfrtxk9h.api.lncld.net/1.1/classes/Zwbbf',
          json: true,
          headers: {
               "Content-Type": "application/json",
               "X-LC-Key": "v9KAOdcB6gaFH5nsTOgBgEds",
               "X-LC-Id": "TfRTxk9HAm2hlkwORYJ6hrKt-gzGzoHsz",
          }, body: {
               "keyname":zhendsss.zuoweibminz,"zuoweib":zhendsss.desserts,"ksheader":zhendsss.exevls
          }
     }, function (err, res, body) {
          console.log(body)
          zhendsss.snackbar=true
          zhendsss.snackbartext="座位表特征码为："+body.objectId
    zhendsss.dengdai=false

     });





                
              });


      },
      sczuoweibyp(){
        this.$db.get('zuowei')
  .remove({ name: 'zuoweidb' })
  .write()
        this.dengdai=true
          this.desserts=[{}]
          this.exevls=['考试教室：','年级：','起止学号：',"科目：","人数：","考试时间："]
          var zwbxx=this.zuoweibxx
          var zhendethis=this
          var qxbs=zwbxx[0].split("-")
          if (new Date().getHours()<=11){
        var sdba = ["6eqige2c", "6EqIge2Ck30wPP37NtdBID5g-gzGzoHsz","TBGPLHrBadoGBt8NXFHs2bEI"]
      }else{
        var sdba = ["gx84kt3l", "Gx84kt3L3sNtFh6N9lR1Wu4k-gzGzoHsz", "iYuza304Ehyq4LG7oe0nFF6C"]
      }
        
          this.$http({
          method: "POST",
          url: '  https://'+sdba[0]+'.engine.lncld.net/1.1/functions/gdmudscs',
          json: true,
          headers: {
               "Content-Type": "application/json",
               "X-LC-Key": sdba[2],
               "X-LC-Id": sdba[1],
          }, body: {
               "csxh":qxbs[0],"jsxh":qxbs[1]
          }
     }, function (err, res, body) {
          console.log(body)
          zhendethis.desserts=body.result
          zhendethis.exevls=['考试教室：'+zwbxx[1],'年级：'+zwbxx[3],'起止学号：'+zwbxx[0],"科目："+zwbxx[2],"人数："+body.result.length,"考试时间："+zwbxx[4]+"\n"+zwbxx[5]]
          zhendethis.dengdai=false
          zhendethis.havefb=true
          zhendethis.$db.read().get('zuowei')
  .push({ name: 'zuoweidb', value: [zhendethis.exevls,body.result]})
  .write()
     });


      }

,

      initialize () {

        if (this.$db.read().get('zuowei').value()==undefined){
  this.$db.defaults({
	zuowei: []
}).write()

this.desserts = [{}]
this.havefb = false

}else{
  var gerenxx=this.$db.read().get('zuowei').value()[0]
  this.desserts = gerenxx?gerenxx.value[1]:[{}]
  this.exevls = gerenxx?gerenxx.value[0]:['考试教室：','年级：','起止学号：',"科目：","人数：","考试时间："]
  this.havefb = gerenxx?true:false
}


      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.desserts.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
        
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      },openfile(){

          shell.showItemInFolder(remote.app.getPath("desktop")+"/座位表.xlsx")
          
      }
    }
  }
</script>
<style>
  

  .card--flex-tor {
    margin-top: 30px;
  }
</style>