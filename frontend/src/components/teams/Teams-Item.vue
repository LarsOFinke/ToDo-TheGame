<template>
    <div class="w-full max-w-sm bg-gray-200 rounded-lg shadow-md p-4 mx-auto relative">
        <!-- Teams-Header -->
        <div class="flex items-center justify-between w-full mb-2">
            <h3 class="text-xl font-bold text-gray-800 mb-2">{{ props.team.name }}</h3>
        </div>

        <!-- Teams-Info -->
        <div class="w-full max-w-sm bg-gray-100 rounded-lg shadow-md p-2 mx-auto relative mb-2">
            <div class="text-sm mb-4 overflow-x-auto  max-h-57">
                <div class="flex text-xs mb-4">
                    <div class="flex flex-col w-35">
                        <label class="mb-2"><u>Founder:</u> Name</label>
                        <label class="mb-2"><u>Info#2:</u> Infopjmdnipsanpid</label>
                        <label class="mb-2"><u>Info#3:</u> KLloihsdulif sdagf ghrdg</label>
                        <label class="mb-2"><u>Info#2:</u> Infopjmdnipsanpid</label>
                        <label class="mb-2"><u>Info#3:</u> KLloihsdulif sdagf ghrdg</label>
                        <label class="mb-2"><u>Info#2:</u> Infopjmdnipsanpid</label>
                        <label class="mb-2"><u>Info#3:</u> KLloihsdulif sdagf ghrdg</label>
                        <label class="mb-2"><u>Info#4:</u> Ohouibhg oughns ubnsgu bdgub klbgu kubgk g jkkjbb hb</label>
                    </div>
                    <div class="flex float-right mr-1">
                        <div class="w-full">
                            <label class="text-sm font-semibold">Members:</label>
                            <p class="text-sm text-right">27</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>


        <!-- Utility-Buttons -->
        <div class="mb-2 absolute top-2 right-2">
            <button type="button"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Details</button>
        </div>
        <div class="w-full flex justify-around">
            <button type="button" @click.prevent="showTeamTasks"
                class="w-fit bg-indigo-600 text-white py-1 px-2 rounded-md hover:bg-indigo-800 transition">Team-Tasks</button>
        </div>
    </div>
</template>

<script setup>


const props = defineProps({
    team: Object
})

const emit = defineEmits(['hideTeamTasks'])

const showTeamTasks = () => {
    emit('hideTeamTasks', [false, props.team.id])
}
</script>