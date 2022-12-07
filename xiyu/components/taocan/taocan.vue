<template>
	<view class="">
		<view class="box" v-for="item,id in taocanList" :key="id">
			<view class="left">
				<image :src="'/static/taocan/' + item.tc_pic" mode="aspectFit" class="taocan" lazy-load></image>
			</view>
			<view class="main">
				<view class="top">
					<h4>{{item.tc_name}}</h4>
					<view class="subtitle">已售：{{item.tc_sale}}</view>
				</view>	
				<view class="middle">
					{{item.tc_price}}元/次  {{item.tc_time}}分钟
				</view>	
				<view class="bottom">
					{{item.tc_intraduce}}
				</view>	
			</view>
			<view class="right">
				<button type="primary" size="mini">预约</button>
			</view>
		</view>
	</view>
	
</template>

<script>
	export default {
		name:"taocan",
		props:{
			taocanList:Array
		},
		data() {
			return {
				
			};
		}
	}
</script>

<style lang="scss">
	.box{
		// background-color: #ccc;
		display: flex;
		height: 200rpx;
		align-items: center;
		text-align: center;
		border-bottom: 1rpx solid #ccc;
		padding: 20rpx 15rpx;
		.left{
			width: 150rpx;
			.taocan{
				width: 150rpx;
				height: 150rpx;
			}
		}
		.main{
			flex-grow: 1;
			display: flex;
			flex-direction: column;
			justify-content: space-around;
			height: 200rpx;
			padding: 10rpx;
			text-align: left;
			.top{
				display: flex;
				justify-content: space-between;
				.subtitle{
					color:gray;
				}
			}
			.middle{
				color: indianred;
			}
			.bottom{
				font-size: 24rpx;
				color: gray;
			}
		}
		.right{
			width: 150rpx;
			align-self: flex-start;
		}
	}
</style>