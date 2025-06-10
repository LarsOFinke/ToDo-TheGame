<template>
    <div class="w-full max-w-sm bg-gray-200 rounded-lg shadow-md p-4 mx-auto relative">
        <!-- Teams-Header -->
        <div class="flex items-center justify-between w-full mb-2">
            <h3 class="text-xl font-bold text-gray-800 mb-2">Team name</h3>
        </div>

        <!-- Teams-Info -->
        <div class="flex text-xs mb-4">
            <div class="flex flex-col w-45">
                <label class="mb-2"><u>Founder:</u> Name</label>
                <label class="mb-2"><u>Info#2:</u> Infopjmdnipsanpid</label>
                <label class="mb-2"><u>Info#3:</u> KLloihsdulif sdagf ghrdg</label>
                <label class="mb-2"><u>Info#4:</u> Ohouibhg oughns ubnsgu bdgub klbgu kubgk g jkkjbb hb</label>
            </div>
            <div class="flex float-right">
                <div class="w-full">
                    <label class="text-sm font-semibold">Members:</label>
                    <p class="text-sm text-right">27</p>
                </div>
            </div>
        </div>

        <!-- Utility-Buttons -->
        <div class="mb-2 absolute top-2 right-2">
            <button type="button"
                class="w-fit bg-indigo-600 text-white py-1 px-4 rounded-md hover:bg-indigo-800 transition">Details</button>
        </div>
        <div class="w-full flex justify-around">
            <button type="button"
                class="w-fit bg-green-600 text-white py-1 px-2 rounded-md hover:bg-green-800 transition">Team-Tasks</button>
        </div>
    </div>
</template>

<script setup>


defineProps({
    team: Object
})
</script>