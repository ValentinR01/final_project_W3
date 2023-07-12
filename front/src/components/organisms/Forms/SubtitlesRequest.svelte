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
  <CheckboxForm data={languages} disabled={disabled} catForm='subtitles'> Demande sous-titres aditionnels </CheckboxForm>
  <Button class='block-center' marginTop='var(--spacing-4)'>Valider</Button>
</form>
