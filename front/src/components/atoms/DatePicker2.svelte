<script>
  import { DateInput, localeFromDateFnsLocale } from 'date-picker-svelte'
  import { fr } from 'date-fns/locale'

  let date = new Date()
  const minDate = {min: date};

  let dateFnsLocale = fr;
  $: locale = localeFromDateFnsLocale(dateFnsLocale);

</script>
  
<DateInput 
  bind:value={date}
  min={minDate.min}
  format="dd/MM/yyyy"
  visible={true}
  closeOnSelection={true}
  {locale}
/>

<style>
  :root {
    --date-picker-highlight-border: none;
    --date-picker-highlight-shadow: none;
    --date-picker-selected-color: var(--blue-base);
    --date-picker-selected-background: var(--lighter-blue);
    --date-input-width: 300px;
  }
</style>