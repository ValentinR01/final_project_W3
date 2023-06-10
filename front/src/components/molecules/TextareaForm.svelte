<script>
  import TextArea from "../atoms/Text-Area.svelte";

  export let name = '';
</script>
  
<div class="textarea-form">
  <label for={name} class="text-preset-4"> <slot /> </label>
  <TextArea />
</div>

<style>
  .textarea-form{
    display: inline-grid;
  }

  label{
    margin-bottom: 5px;
  }
</style>