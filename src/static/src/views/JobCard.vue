<template>
  <b-card :title="jobName"
          img-src="https://lorempixel.com/600/300/food/5/"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2">
    <p class="card-text">
      {{jobDesc}}
    </p>
    <b-button :href=jobExecCall variant="primary">Executar</b-button>
  </b-card>
</template>

<script>
export default {
  name: 'jobCard',
  props: ['jobName', 'jobDesc', 'jobExecCall']
}
</script>
