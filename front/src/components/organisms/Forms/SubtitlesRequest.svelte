<script>

  import Button from "../../atoms/Button.svelte";
import CheckboxForm from "../../molecules/formFields/CheckboxForm.svelte";

  /**
   * @type {any}
  */
  export let data;

  /**
   * @type {any}
  */
  export let languages;

  export let disabled = ["Français","Anglais"];

</script>

<form method="POST">
  <div class='form-subtitles'>
    <CheckboxForm data={languages} disabled={disabled} catForm='subtitles'> Demande sous-titres aditionnels </CheckboxForm>
  </div>
  <Button class='block-center'>Valider</Button>
</form>

<style>
  .form-subtitles{
    margin: var(--spacing-4) 0;
  }
</style>