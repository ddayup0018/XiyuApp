<template>
	<view class="box">
		<view class="item" v-for="(item,index) in headerList" :key="index">
			<view :class="ischecked == index ? 'active' : 'default'" @click="checked(index)">
				{{item.status}}
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		name:"headerbar",
		props:{
			ischecked:Number,
			headerList:Array
		},
		data() {
			return {
				
			};
		},
		methods:{
			checked(val){
				console.log(val)
				this.$emit('childChecked',val)
			},
		}
	}
</script>

<style lang="scss">
	.box{
		// background-color: #ccc;
		display: flex;
		justify-content: space-around;
		align-items: center;
		text-align: center;
		width: 100%;
		border-bottom: 1rpx solid #ccc;
		.item{
			width: 50%;
			height: 70rpx;
			line-height: 70rpx;
			.active{
				// background-color: blue;
				color: blue;
				border-bottom: 1rpx solid blue;
				
			}
			.default {
				// background-color: #ccc;
				border-bottom: #ccc;
			}
		}
	}

</style>