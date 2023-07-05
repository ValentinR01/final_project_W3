<script>
  import Button from "../../atoms/Button.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";

  export let data;

  
  /**
   * @type {{ error: any; }}
  */
  //export let form;

</script>

<!--
{#if form?.error}
  <p class="error">{form.error}</p>
{/if}
-->

<form method="POST" action='?/create'>
  <div class='form-intevenor'>
    <InputForm name="name"> Name </InputForm>
  </div>
  <Button class='block-center'> Valider </Button>
</form>

<style>
  .form-intevenor{
    margin: var(--spacing-3) 0;
  }
</style>