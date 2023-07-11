<script>
  import Button from "../../atoms/Button.svelte";
  import InputForm from "../../molecules/formFields/InputForm.svelte";
  
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
  <InputForm id="name" name="name"> Name </InputForm>
  <Button class='block-center' marginTop='var(--spacing-3)'> Valider </Button>
</form>