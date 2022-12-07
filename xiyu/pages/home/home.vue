<template>
	<view class="outer">
		<view class="header">
			<swiper
			circular 
			indicator-dots="true" 
			autoplay="true" 
			interval="3000" 
			duration="1000">
				<swiper-item v-for="(item,index) in swiperList" :key="index">
					<image :src="item.url" mode="" class="swiper-img"></image>
				</swiper-item>
			</swiper>
		</view>
		<view class="body">
			<!-- <view class="" v-for="item,id in taocanList" :key="id"> -->
				<taocan 
				:taocanList="taocanList"
				></taocan>
			<!-- </view> -->
		</view>
	</view>
</template>

<script>
	import taocan from '@/components/taocan/taocan.vue'
	export default {
		components:{
			taocan
		},
		data() {
			return {
				username:'',
				swiperList:[
					{url:'/static/swiper/swiper1.png'},
					{url:'/static/swiper/swiper2.png'},
					{url:'/static/swiper/swiper3.png'}
				],
				taocanList:[]
			}
		},
		onLoad(){
			let user = this.$config.user.get_user()
			console.log(user)
		},
		onShow(){
			
			
			this.getTaocan()
			
		},
		methods: {
			login(){
				uni.navigateTo({
					url:'/pages/login/login'
				})
			},
			logout(){
				this.username=''
				this.$config.user.clear_user()
				plus.runtime.quit()
			},
			async getTaocan(){
				const res = await this.$http({
					url:'/gettaocanlist/',
					method:'GET'
				})
				console.log(res.data.msg)
				if (res.data.code == 1){
					this.taocanList = res.data.msg
				}
			}
		}
	}
</script>

<style lang="scss">
	.outer{
		padding: 0;
		margin: 0;
		box-sizing: border-box;
		.header{
			.swiper-img{
				width: 100%;
				height:300rpx;
			}
		}
		.body{
			
		}
		
	}
</style>
