<script>
  import Margin from '../../../components/atoms/Margin.svelte';
  import ProjectCreationForm from '../../../components/organisms/Forms/ProjectCreationForm.svelte';

  export let data;
</script>

<Margin marginTop='3%'>
  <div class='card card--wide block-center'>
    <ProjectCreationForm data={data}/>
  </div>
</Margin>