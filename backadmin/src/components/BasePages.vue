<template>
  <el-container>
    <el-header>
      <div class="title">妈咪端后台管理系统</div>
      <div class="userinfo">
        <el-dropdown>
          <span class="el-dropdown-link">
            用户信息<i class="el-icon-arrow-down el-icon--right"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>添加用户</el-dropdown-item>
            <el-dropdown-item>修改信息</el-dropdown-item>
            <el-dropdown-item>退出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      </el-header>
      <div class="mymain">
        <el-aside>
            <MyNavMenu/>
        </el-aside>
        <el-main>
          <router-view v-if="isRouterAlive"></router-view>
        </el-main>
      </div>
  </el-container>
</template>

<script>
import MyNavMenu from '@/components/MyNavMenu.vue'
  export default {
    components:{
      MyNavMenu
    },
    data(){
      return {
        isRouterAlive:true
      }
    },
    provide(){
      return {
        reload:this.reload
      }
    },
    methods:{
      reload(){
        this.isRouterAlive = false
        this.$nextTick(()=>{
          this.isRouterAlive = true
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
  .el-container{
    height: 100vh;
    width:100vw;
    .el-header{
      background-color: #eee;
      display: flex;
      justify-content: space-between;
      align-items: center;
      .title{
        font-size: 24px;
        font-weight: 700;
        color: palevioletred;
      }
      .userinfo{
        .el-dropdown-link {
          cursor: pointer;
        }
        .el-icon-arrow-down {
          font-size: 12px;
        }
      }
    }
    .mymain{
      display: flex;
      flex-grow: 1;
      .el-aside{
        background-color: red;
        }
      .el-main{
        // background-color: #ccc;
        width: 100%;
      }
    }
  }
  
  
</style>