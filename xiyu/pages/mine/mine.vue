<template>
	<view class="outer">
		<view class="header">
			<view class="">
				<uni-card 
				:title="userInfo.userName" 
				:sub-title="userInfo.userLevel" 
				:extra="userInfo.userMoney+'元'" 
				:thumbnail="userInfo.avatar">
					<uni-section title="个性标签" type="line">
						<view class="example-body" >
							<blockquote v-for="item,index in userInfo.userCharacter" :key="index">
								<view class="tag-view">
									<uni-tag :inverted="true" :text="item.name" :type="item.type" />
								</view>
							</blockquote>
						</view>
					</uni-section>
					<uni-list>
						<uni-list-item title="充值加油" showArrow 
						to="/pages/mine/recharge/recharge" ></uni-list-item>
						<uni-list-item title="消息推送" 
						showSwitch switchChecked @switchChange="switchChange"></uni-list-item>
						<uni-list-item title="修改密码" showArrow 
						to="/pages/mine/updatePwd/updatePwd"></uni-list-item>
						<uni-list-item title="安全退出" showArrow clickable @click="appQuit"></uni-list-item>
					</uni-list>
				</uni-card>
			</view>
		</view>
		<view class="bottom">
			<view class="bottom-box" @click="calMyPhone(myphone)">
				<view>
					<uni-icons type="phone" color="#fff" size="24"></uni-icons>
					<text>销售热线：{{myphone}}</text>
					
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				userInfo:{
					avatar:'/static/logo.png',
					userName:'19216811255',
					userLevel:'黄金会员',
					userMoney:80.38,
					userCharacter:[
						{name:'热情',type:'error'},
						{name:'高素质',type:'primary'},
						{name:'土肥圆',type:'success'},
					]
				},
				myphone:'12345678'
				
			}
		},
		methods: {
			calMyPhone(val){
				// #ifdef APP-PLUS
				console.log('打电话'+val)
				uni.makePhoneCall({
					phoneNumber:val
				})
				// #endif
				// #ifdef H5
				console.log('我是打电话，但是我打不起')
				// #endif
			},
			appQuit(){
				// #ifdef APP-PLUS
				if (uni.getSystemInfoSync().platform == "android") {
					plus.runtime.quit();
				}
				// #endif
				// #ifdef H5
				console.log('我是退出，但是我退不起')
				// #endif
			},
			switchChange(e){
				// console.log(e.value)
				if(e.value == true){
					console.log('用户打开了消息推送')
				}else{
					console.log('用户关闭了消息推送')
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
	width: 100%;
	min-height: 100%;
	
	.header{
		.example-body{
			margin-bottom: 60rpx;
			display: flex;
			.tag-view{
				margin: 0 20rpx;
			}
		}
	}
	
	.bottom{
		color:#fff;
		text-align: center;
		font-size: 32rpx;
		font-weight: 700;
		margin-top: 80rpx;
		position: relative;
		height: 100rpx;
		
		.bottom-box{
			// 固定位置，会遮挡内容
			// position: fixed;
			// left:50%;
			// top:80%;
			// transform: translate(-50%,-50%);
			
			// 相对父盒子位置，不会遮挡内容
			position: absolute;
			left: 50%;
			top: 50%;
			transform: translate(-50%,-50%);
			background-color: #2490ff;
			width: 75%;
			height: 100rpx;
			line-height: 100rpx;
			border-radius: 50rpx;
			
		}
	}
	
}
</style>
