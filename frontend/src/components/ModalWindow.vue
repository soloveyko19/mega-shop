<template>
    <div class="modal">
        <div class="blank__space" @click="exit">
            <div class="window" @click.stop>
                <div class="exit_button_box">
                    <button class="exit_button" @click="exit">
                        <div class="close_image_box">
                            <img :src="CloseCircleImage" alt="close circle">
                        </div>
                    </button>
                </div>
                <slot />
            </div>
        </div>
    </div>
</template>


<script lang="ts" setup>
import CloseCircleImage from '~/assets/img/close-circle.svg'
interface Props {
    exit: () => void
}
const { exit } = defineProps<Props>()

</script>


<style lang="css" scoped>
.modal {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100vh;
}

.blank__space {
    width: 100%;
    height: 100vh;
    background-color: rgba(33, 33, 33, 0.2);
    backdrop-filter: blur(4px);
    display: flex;
    align-items: center;
    justify-content: center;
}

.window {
    background-color: rgb(220, 220, 220);
    min-height: 200px;
    min-width: 100px;
    padding: 15px;
    padding-top: 40px;
    border: 1px solid rgb(33, 33, 33);
    border-radius: 5px;
    position: relative;
}

.exit_button_box {
    position: absolute;
    top: 5px;
    right: 5px;
}

.exit_button {
    border: none;
    background-color: transparent;
    cursor: pointer;
}

.close_image_box {
    width: 30px;
    height: 30px;
}

.close_image_box img {
    width: 100%;
    height: 100%;
}
</style>