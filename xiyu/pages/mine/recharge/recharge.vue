<template>
	<view class="outer">
		<h1>余额充值</h1>
		<view class="box">
			<view class="item">
				<uni-easyinput  prefixIcon="person" v-model="FormData.userName" type="text" disabled/>
			</view>
			<view class="item">
				<uni-easyinput  prefixIcon="wallet" v-model="FormData.rechargeMoney" placeholder="请输入充值金额" type="number"/>
			</view>
			<view class="item">
				<button type="primary" @click="recharge">充值</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				FormData:{
					rechargeMoney:'',
					userName:'123456'
				}
			}
		},
		methods: {
			async recharge(){
				if (!this.FormData.rechargeMoney){
					uni.showToast({
						title: '充值数量不能为空',
						icon:'none'
					});
					return
				}
				// const res = await this.$http({
				// 	url:'/login/',
				// 	method:'POST',
				// 	data:this.FormData
				// })
				// if (res.data.code == 1){
				// 	console.log(res.data.msg)
					
				// 	this.$config.user.set_user(res.data.msg.username,res.data.msg.token)
				// 	uni.switchTab({
				// 		url:'/pages/home/home'
				// 	})
					
				// }else {
				// 	uni.showToast({
				// 		title:res.data.msg,
				// 		icon:'none',
				// 		duration:2000
				// 	})
				// }
			}
		}
	}
</script>

<style lang="scss">
	.outer{
		padding: 0;
		margin: 0;
		box-sizing: border-box;
		h1{
			text-align: center;
			margin: 80rpx;
		}
		.box{
			width: 80%;
			margin: 0 auto;
			.item{
				margin-top: 50rpx;
			}
		}
	}
</style>



