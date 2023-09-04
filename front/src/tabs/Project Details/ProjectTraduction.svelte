<script>
  import Button from "../../components/atoms/Button.svelte";
  import Margin from "../../components/atoms/Margin.svelte";
  import Text from "../../components/atoms/Text.svelte";
  import CheckboxForm from "../../components/molecules/formFields/CheckboxForm.svelte";

  /**
   * @type {{ asset: { translations: any[]; }[]; metadata: { translations: any; }; }}
   */
   export let data;
</script>

<Text
  textTag='p'
  class='text-preset-4'
>
  Langue de la vidéo : {data.asset[1].translations[0]}
</Text>

<Margin marginTop='var(--spacing-3)' marginBottom='var(--spacing-3)'>
  <Text
    textTag='p'
    class='text-preset-4'
  >
    Langue sous-titres actuels : {data.asset[1].translations[0]}
  </Text>
</Margin>

<form>
  <CheckboxForm data={data.metadata.translations} catForm='sous-titres'> Demande sous-titres additionnels : </CheckboxForm>
  <Button class='block-center' marginTop='var(--spacing-3)'> Valider </Button>
</form>