<template>
	<view class="outer">
		<view class="header">
			<headerbar 
			:ischecked="ischecked" 
			:headerList="headerList" 
			@childChecked="checked"></headerbar>
		</view>
		<view class="body">
			<jishione :jishiList="jishiList" :ischecked="ischecked"></jishione>
		</view>
	</view>
</template>

<script>
	import jishione from '@/components/jishione/jishione.vue'
	import headerbar from '@/components/headerbar/headerbar.vue'
	export default {
		components:{
			jishione,
			headerbar
		},
		data() {
			return {
				ischecked:0,
				headerList:[
						{status:'空闲'},
						{status:'上钟'},
					],
				jishiList:[]
			}
		},
		onShow() {
			this.getJishi()
		},
		methods: {
			checked(retdata){
				// this.$refs.child.checked()
				console.log(retdata)
				this.ischecked=retdata
			},
			async getJishi(){
				const res = await this.$http({
					url:'/getjishilist/',
					method:'GET'
				})
				console.log(res.data.msg)
				if (res.data.code == 1){
					this.jishiList = res.data.msg
				}
			}
		},
		onPullDownRefresh() {
			console.log('刷新')
			this.getJishi()
			uni.stopPullDownRefresh()
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

		}
	}
</style>
