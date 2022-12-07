<template>
	<view>
		<view class="box">
			<view class="box-item" 
			v-for="(item,id) in jishiList" :key="id" 
			v-if="item.js_status =='空闲'?ischecked==0:ischecked==1">
				<view class="left">
					<image :src="'/static/jishi/' + item.js_pic" mode="" class="box-img"></image>
				</view>
				<view class="middle">
					<h4>技师简介</h4>
					<h5>姓名:{{item.js_name}}</h5>
					<h5>来自:{{item.js_from}}</h5>
					<h5>特长:{{item.js_specialty}}</h5>
					<h5>当前状态：{{item.js_status}}</h5>
				</view>
				<view class="right">
					<button type="primary" size="mini" v-if="item.js_status =='空闲'">点我</button>
					<button type="primary" size="mini">约我</button>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"jishione",
		props:{
			ischecked:Number,
			jishiList:Array
		},
		data() {
			return {
				
			};
		}
	}
</script>

<style lang="scss">
.box{
	.box-item{
		display: flex;
		justify-content: space-around;
		text-align: center;
		align-items: center;
		padding: 10rpx 0;
		border-bottom: 1rpx solid #ccc;
		.left{
			width: 200rpx;
			height: 200rpx;
			margin-right: 20rpx;
			.box-img{
				width: 100%;
				height: 100%;
				border-radius: 50%;
			}
		}
		.middle{
			flex-grow: 1;
			height: 240rpx;
			// background-color: red;
			display: flex;
			flex-direction: column;
			h5{
				text-align: left;
				margin: 2rpx 20rpx;
			}
		}
		.right{
			width: 150rpx;
			align-self:center
		}
	}
	}
</style>