<template>
	<view class="outer">
		<view class="header">
			<headerbar 
			:ischecked="ischecked" 
			:headerList="headerList" 
			@childChecked="checked"></headerbar>
		</view>
		<view class="body">
			<view class="" 
			v-for="(item,id) in dingList" :key="id" 
			v-if="item.ding_status == '进行中'? ischecked == 0 : ischecked == 1">
				<uni-card :title="item.tc_name" :sub-title="item.js_name" :extra="item.ding_status" :thumbnail="'/static/jishi/' + item.js_pic">
					<view class="uni-body">
						<view class="">套餐价格：{{item.tc_price}}元</view>
						<view class="">套餐时间：{{item.tc_time}}分钟</view>
						<view class="">套餐介绍：{{item.tc_intraduce}}</view>
						<view class="">
							<text>技师留言：贵宾请您耐心等待，妹妹已经出发啦！</text>
						</view>
						<view class="btn-box" v-if="item.ding_status == '进行中'">
							<button type="primary" size="mini" @click="serverClick(item.id)">开始服务</button>
							<button type="primary" size="mini">我要加钟</button>
							<button type="primary" size="mini">取消订单</button>
						</view>
						<!-- <view class="btn-box" v-if="item.ding_status == '已完成'"> -->
						<view class="btn-box" v-else>
							<button type="primary" size="mini">我要评价</button>
							<button type="primary" size="mini">再来一单</button>
						</view>
					</view>
				</uni-card>
			</view>
			
		</view>
	</view>
</template>

<script>
	import jishione from '@/components/jishione/jishione.vue'
	import headerbar from '@/components/headerbar/headerbar.vue'
	export default {
		components:{
			headerbar
		},
		data() {
			return {
				ischecked:0,
				headerList:[
						{status:'进行中'},
						{status:'已完成'},
					],
				dingList:[
					// {
					// 	id:1,
					// 	ding_status:'进行中',
					// 	startServer:false,
					// 	js_pic:'/static/jishi/jishi4.png',
					// 	js_name:'三上',
					// 	tc_name:'五感奢宠定制',
					// 	tc_price:'699',
					// 	tc_time:'120',
					// 	tc_intraduce:'全身精油按摩+头疗+多处护理'
					// },
					// {
					// 	id:2,
					// 	ding_status:'已完成',
					// 	startServer:false,
					// 	js_pic:'/static/jishi/jishi3.png',
					// 	js_name:'李上钟',
					// 	tc_name:'五感奢宠定制',
					// 	tc_price:'699',
					// 	tc_time:'120',
					// 	tc_intraduce:'全身精油按摩+头疗+多处护理'
					// }
				],
				
			}
		},
		onShow(){
			this.getDingdan()
			
		},
		computed:{
			
		},
		methods: {
			checked(retdata){
				// this.$refs.child.checked()
				console.log(retdata)
				this.ischecked=retdata
			},
			serverClick(val){
				console.log(val)
			},
			async getDingdan(){
				let user = this.$config.user.get_user()
				console.log(user)
				console.log(user.uid)
				const res = await this.$http({
					url:'/getdinglist/',
					method:'GET',
					data:user
				})
				console.log(res.data.msg)
				this.dingList = res.data.msg
			}
		},
		onPullDownRefresh() {
			console.log('刷新')
			this.getDingdan()
			uni.stopPullDownRefresh()
			console.log('刷新完成')
		}
	}
</script>

<style lang="scss">
	.outer{
		padding: 0;
		margin: 0;
		box-sizing: border-box;
		.header{
			
		}
		.body{
			margin: 20rpx;
			.uni-body{
				font-size: 20rpx;
				.btn-box{
					display: flex;
					justify-content: space-around;
					margin-top: 30rpx;
				}
			}

		}
	}
</style>

