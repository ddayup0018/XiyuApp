<template>
    <el-menu
      default-active="2"
      class="el-menu"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      router>
      <el-menu-item index="/home" >
        <i class="el-icon-setting"></i>
        <span slot="title">主页</span>
      </el-menu-item>
      <el-menu-item index="/taocan">
        <i class="el-icon-setting"></i>
        <span slot="title">套餐管理</span>
      </el-menu-item>
      <el-menu-item index="/jishi">
        <i class="el-icon-setting"></i>
        <span slot="title">技师管理</span>
      </el-menu-item>
      <el-menu-item index="/user">
        <i class="el-icon-setting"></i>
        <span slot="title">用户管理</span>
      </el-menu-item>
      
    </el-menu>
</template>

<script>
  export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>

<style lang="scss" scoped>
    .el-menu{
        height: 100%;
    }
</style>