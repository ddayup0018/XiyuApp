<template>
  <div>
    <h1>套餐管理</h1>
    <el-button type="primary" @click="test">查询一个</el-button>
    <div class="insertbtn">
      <el-button type="success" @click="dialogVisible = true">新增套餐</el-button>
    </div>
    <el-dialog
      :title="btnType == 0 ? '新增' : '修改'"
      :visible.sync="dialogVisible"
      width="30%">
      <el-input v-model="form.tc_name" placeholder="套餐名称"></el-input>
      <el-input v-model="form.tc_time" placeholder="套餐时间"></el-input>
      <el-input v-model="form.tc_price" placeholder="套餐价格"></el-input>
      <el-input v-model="form.tc_intraduce" placeholder="套餐介绍"></el-input>
      <el-input v-model="thisid" disabled v-if="btnType == 1"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="insertTaocan()" v-if="btnType == 0">新增</el-button>
        <el-button type="primary" @click="editTaocan(thisid)" v-if="btnType == 1">修改</el-button>
      </span>
    </el-dialog>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
          prop="id"
          label="套餐id">
        </el-table-column>
        <el-table-column
          prop="tc_name"
          label="套餐名称">
        </el-table-column>
        <el-table-column
          prop="tc_sale"
          label="套餐销售量">
        </el-table-column>
        <el-table-column
          prop="tc_price"
          label="套餐价格">
        </el-table-column>
        <el-table-column
          prop="tc_time"
          label="套餐时间">
        </el-table-column>
        <el-table-column
          prop="tc_intraduce"
          label="套餐介绍">
        </el-table-column>
        <el-table-column
          label="操作项">
          <template slot-scope="scope">
            <el-button type="primary" plain @click="editthis(scope.row)">修改</el-button>
            <el-button type="danger" plain @click="deletethis(scope.row.id)">删除</el-button>
          </template>
        </el-table-column>
    </el-table>
  </div>
  
</template>

<script>
import {taocan} from "@/utils/api"
export default {
  inject:['reload'],
  data(){
    return {
      tableData:[],
      dialogVisible: false,
      btnType:0,
      thisid:null,
      form:{
        tc_name :'',
        tc_time :'',
        tc_price :'',
        tc_intraduce :'',
      }
    }
  },
  mounted(){
    taocan.get().then(res=>{
        console.log(res)
        console.log(res.data)
        this.tableData = res.data
    })
    // getRequest('/taocan/').then((res)=>{
    //     console.log('页面打印')
    //     console.log(res.data)
    //     this.tableData = res.data
    // })
  },
  watch:{
    dialogVisible:{
      handler(val){
        console.log(val)
        if (val == false){
          this.btnType = 0
          for (let i in this.form){
            this.form[i] = ''
          }
        }
      },
      immediate: true
    }
  },
  methods:{
      insertTaocan(){
          taocan.post(this.form).then((res)=>{
          console.log(res)
          this.$message({
              message:'提交成功！',
              type:'success'
            })
          this.dialogVisible =false
          })
          this.reload()
      },
      editTaocan(id){
          taocan.put(id,this.form).then((res)=>{
          console.log(res)
          this.$message({
              message:'修改成功！',
              type:'success'
            })
          this.dialogVisible =false
          })
          this.reload()
      },
      editthis(val){
        this.dialogVisible =true
        this.btnType = 1
        this.thisid = val.id
        this.form.tc_name = val.tc_name
        this.form.tc_time = val.tc_time
        this.form.tc_price = val.tc_price
        this.form.tc_intraduce = val.tc_intraduce
      },
      // deletethis(id){
      //   // deleteRequest(`/taocan/${id}/`).then((res)=>{
      //   //   console.log(res)
      //   deleteRequest(`/taocan/`).then((res)=>{
      //     if (res.status == 204){
      //         this.$message({
      //           message:'删除成功！',
      //           type:'success'
      //         })
      //       }
      //       this.reload()
      //   })
      // }
      deletethis(id){
        taocan.delete(id).then(res=>{
          console.log(res.status)
          if (res.status == 204){
              this.$message({
                message:'删除成功！',
                type:'success'
              })
            }
            this.reload()
        })
      },
      test(){
        taocan.get().then(res=>{
          console.log(res.data)
        })
      }

      
    }
  }
</script>

<style lang="scss" scoped>
.el-input{
  margin: 10px 0;
}
.insertbtn{
  margin: 20px;
}
h1{
  text-align: center;
}
</style>