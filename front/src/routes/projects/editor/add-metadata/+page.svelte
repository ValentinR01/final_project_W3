<script>
  import Margin from '../../../../components/atoms/Margin.svelte';
  import ProjectEditionForm from '../../../../components/organisms/Forms/ProjectEditionForm.svelte';

  export let data;
</script>

<Margin marginTop='3%'>
  <div class='card card--wide block-center'>
    <ProjectEditionForm data={data} />
  </div>
</Margin>

<style>

</style>