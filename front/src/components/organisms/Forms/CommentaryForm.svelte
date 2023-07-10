<script>
  import Button from "../../atoms/Button.svelte";
  import TextArea from "../../atoms/Text-Area.svelte";
  import InputForm from "../../molecules/InputForm.svelte";

  export let userComment = 'existing';
</script>

<form class="commentary-form">
  {#if userComment == 'new'}
    <InputForm id="name" name="name"> Nom </InputForm>
  {/if}
  <TextArea placeholder="Ecrire un commentaire..." />
  <Button marginTop="var(--spacing-1)"> Valider </Button>  
</form>

<style>
  .commentary-form{
    display: flex;
    flex-wrap: wrap;
    justify-content: end;
    row-gap: var(--spacing-2);
  }

  .commentary-form :global(textarea){
    padding: var(--spacing-3);
  }
</style>